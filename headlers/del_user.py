from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
import psutil


async def del_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_authorized(update.effective_user.id):
        return await update.message.reply_text("🚫 Доступ запрещён.")
    
    if len(context.args) < 1:
        return await update.message.reply_text("Использование: /deluser username")
    
    username = context.args[0]

    try:
        result = subprocess.run(
            ["./delete_user.sh", username],
            capture_output=True, text=True, check=True
        )
        await update.message.reply_text(f"✅ Пользователь {username} удалён.\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        await update.message.reply_text(f"❌ Ошибка удаления пользователя:\n{e.stderr}")

def get_deluser_handler():
    return CommandHandler("deluser", del_user)