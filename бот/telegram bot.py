import os
from random import choice
from telegram.ext import Updater, CommandHandler, Job
from datetime import time

# Путь к папке с картинками
IMAGES_DIR = 'images'

# Время для отправки картинок (12:00)
SEND_TIME = time(12, 0)


# Функция для отправки случайной картинки
def send_image(context):
    chat_id = context.job.context
    image_path = os.path.join(IMAGES_DIR, choice(os.listdir(IMAGES_DIR)))
    with open(image_path, 'rb') as f:
        context.bot.send_photo(chat_id=chat_id, photo=f)


# Функция для запуска периодической отправки картинок
def start_image_sender(update, context):
    chat_id = update.effective_chat.id
    context.job_queue.run_daily(send_image, SEND_TIME, days=(3,), context=chat_id)


# Функция для остановки периодической отправки картинок
def stop_image_sender(update, context):
    chat_id = update.effective_chat.id
    current_jobs = context.job_queue.get_jobs_by_name(str(chat_id))
    for job in current_jobs:
        job.schedule_removal()


# Функция-обработчик команд
def command_handler(update, context):
    if update.message.text == '/start':
        start_image_sender(update, context)
    elif update.message.text == '/stop':
        stop_image_sender(update, context)


# Основная функция
def main():
    updater = Updater(token='6333542917:AAGdh5BBimRhs-I7zuty1dfr2GIzhodv8PQ', use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start_image_sender))
    dispatcher.add_handler(CommandHandler('stop', stop_image_sender))
    updater.start_polling()


if __name__ == '__main__':
    main()
