import os
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

ADMIN = [5246802945, 996614218, 6816214702]

def is_authorized(user_id):
    return user_id in ADMIN

async def reboot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_authorized(update.effective_user.id):
        return await update.message.reply_text("🚫 Доступ запрещен.")

    await update.message.reply_text("🔄 Перезагрузка сервера...")
    os.system("reboot")  # осторожно: это реально перезагружает сервер

def get_reboot_handler():
    return CommandHandler("reboot", reboot)
