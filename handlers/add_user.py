from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from app.db import GetDB, crud
from app.db.schemas import UserCreate  # Импорт корректный, проверь у себя
from control import ADMIN

def is_authorized(user_id):
    return user_id in ADMIN

async def add_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_authorized(update.effective_user.id):
        return await update.message.reply_text("🚫 Доступ запрещён.")

    args = context.args
    if len(args) != 3:
        return await update.message.reply_text("❌ Использование: /adduser <имя> <трафик_ГБ> <дней>")

    username, traffic_str, days_str = args

    try:
        traffic = int(traffic_str)
        days = int(days_str)
    except ValueError:
        return await update.message.reply_text("❌ Трафик и срок должны быть числами.")

    # Создаем объект UserCreate с необходимыми полями.
    new_user = UserCreate(
        username=username,
        data_limit=traffic * (1024 ** 3),  # ГБ в байты
        expire=days,
        # Добавь остальные обязательные поля, если нужно
    )

    try:
        with GetDB() as db:
            db_user = crud.create_user(db, new_user)
        await update.message.reply_text(f"✅ Пользователь `{username}` успешно создан.")
    except Exception as e:
        await update.message.reply_text(f"❌ Ошибка при создании пользователя:\n{e}")

def get_add_user_handler():
    return CommandHandler("adduser", add_user)
