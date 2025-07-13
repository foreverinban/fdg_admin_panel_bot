from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
import subprocess
from control import ADMIN

def is_authorized(user_id):
    return user_id in ADMIN

async def add_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_authorized(update.effective_user.id):
        return await update.message.reply_text("🚫 Доступ запрещён.")

    args = context.args
    if len(args) != 3:
        return await update.message.reply_text("❌ Использование: /adduser <имя> <трафик_ГБ> <дней>")

    username, traffic, days = args

    try:
        traffic = int(traffic)
        days = int(days)
    except ValueError:
        return await update.message.reply_text("❌ Трафик и срок должны быть числами.")

    cmd = [
        "docker", "exec", "marzban_marzban_1",
        "python3", "/code/marzban-cli.py", "add-user", username,
        "--limit", str(traffic),
        "--expiry", str(days)
    ]





    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        await update.message.reply_text(f"✅ Пользователь `{username}` создан.\n\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        await update.message.reply_text(f"❌ Ошибка при создании пользователя:\n{e.stderr or e.stdout}")

def get_add_user_handler():
    return CommandHandler("adduser", add_user)
