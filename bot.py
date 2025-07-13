import subprocess
import psutil
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from control import BOT, ADMIN
from handlers.status import get_status_handler
from handlers.add_user import get_adduser_handler
from handlers.del_user import get_deluser_handler

def is_authorized(user_id):
    return user_id in ADMIN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Проверка доступов...")
    if not is_authorized(update.effective_user.id):
        return await update.message.reply_text("🚫 Доступ запрещён.")
    await update.message.reply_text("✅ Доступ разрешён. Привет!")

def main():
    app = ApplicationBuilder().token(BOT).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(get_status_handler())
    app.add_handler(get_adduser_handler())
    app.add_handler(get_deluser_handler())

    app.run_polling()

if __name__ == "__main__":
    main()
