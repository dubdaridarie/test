import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Вставьте сюда ваш токен, полученный от BotFather
BOT_TOKEN = "YOUR_BOT_TOKEN"

# Включаем логирование, чтобы видеть информацию о работе бота
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        f"Привет, {user.mention_html()}! Я простой бот.",
    )
    logger.info(f"Пользователь {user.id} запустил бота")

def main() -> None:
    """Запускает бота."""
    # Создаем приложение и передаем ему токен
    application = Application.builder().token(BOT_TOKEN).build()

    # Регистрируем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота в режиме polling
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()

