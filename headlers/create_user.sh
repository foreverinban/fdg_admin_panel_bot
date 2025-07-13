#!/bin/bash

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 username password"
  exit 1
fi

USERNAME=$1
PASSWORD=$2
DB_PATH="/opt/marzban/db.sqlite3"

# Генерируем хэш пароля Python-скриптом (bcrypt)
HASH=$(python3 -c "import bcrypt; print(bcrypt.hashpw(b'$PASSWORD', bcrypt.gensalt()).decode())")

# Вставляем пользователя в базу SQLite (таблица users, поменяй при необходимости)
sqlite3 "$DB_PATH" <<EOF
INSERT INTO users (username, password_hash) VALUES ('$USERNAME', '$HASH');
EOF

if [ $? -eq 0 ]; then
  echo "User '$USERNAME' added successfully."
else
  echo "Failed to add user."
  exit 2
fi
