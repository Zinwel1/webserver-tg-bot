from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Замените TOKEN на ваш токен бота
TOKEN = '6333542917:AAGdh5BBimRhs-I7zuty1dfr2GIzhodv8PQ'

# Функция-обработчик для команды /start
def start(update: Update, context: CallbackContext) -> None:
    """Отправляет сообщение, когда получена команда /start"""
    user = update.effective_user
    update.message.reply_markdown_v2(
        f'Привет, {user.mention_markdown_v2()}\!',
        reply_markup=None
    )

# Функция-обработчик для команды /hello
def hello(update: Update, context: CallbackContext) -> None:
    """Отправляет сообщение, когда получена команда /hello"""
    update.message.reply_text('Здравствуйте!')

# Функция для обработки ошибок
def error_handler(update: Update, context: CallbackContext) -> None:
    """Логирует ошибки"""
    print(f'Произошла ошибка: {context.error}')

def main() -> None:
    """Запускает бота"""
    updater = Updater(TOKEN)

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчики команд
    start_handler = CommandHandler('start', start)
    hello_handler = CommandHandler('hello', hello)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(hello_handler)

    # Регистрируем обработчик ошибок
    dispatcher.add_error_handler(error_handler)

    # Запускаем бота
    updater.start_polling()

    # Ждем завершения работы бота (например, по нажатию Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()
