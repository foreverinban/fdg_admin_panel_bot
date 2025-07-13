from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
import psutil

ADMIN = [5246802945, 996614218, 6816214702]

# Проверка доступа
def is_authorized(user_id):
    return user_id in ADMIN

# Обработчик /status
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_authorized(update.effective_user.id):
        return await update.message.reply_text("🚫 Доступ запрещен.")
    
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    msg = f"""📊 Статус сервера:
🔸 CPU: {cpu}%
🔸 RAM: {mem.percent}% ({mem.used // (1024**2)} MB / {mem.total // (1024**2)} MB)
🔸 Disk: {disk.percent}% ({disk.used // (1024**3)} GB / {disk.total // (1024**3)} GB)
"""
    await update.message.reply_text(msg)

# Функция возвращает хендлер
def get_status_handler():
    return CommandHandler("status", status)
