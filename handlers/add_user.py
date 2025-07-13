from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
import psutil

async def add_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_authorized(update.effective_user.id):
        return await update.message.reply_text("🚫 Доступ запрещён.")
    
    if len(context.args) < 2:
        return await update.message.reply_text("Использование: /adduser username password")
    
    username = context.args[0]
    password = context.args[1]

    # Пример запуска скрипта для создания пользователя (замени на реальную команду)
    try:
        # Например, есть скрипт create_user.sh который принимает имя и пароль
        result = subprocess.run(
            ["./create_user.sh", username, password],
            capture_output=True, text=True, check=True
        )
        await update.message.reply_text(f"✅ Пользователь {username} создан.\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        await update.message.reply_text(f"❌ Ошибка создания пользователя:\n{e.stderr}")

def get_adduser_handler():
    return CommandHandler("adduser", add_user)