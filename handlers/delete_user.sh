#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 username"
  exit 1
fi

USERNAME=$1
DB_PATH="/opt/marzban/db.sqlite3"

sqlite3 "$DB_PATH" <<EOF
DELETE FROM users WHERE username='$USERNAME';
EOF

if [ $? -eq 0 ]; then
  echo "User '$USERNAME' deleted successfully."
else
  echo "Failed to delete user."
  exit 2
fi
