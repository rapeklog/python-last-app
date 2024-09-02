import telebot
import time

# Здесь вставьте ваш токен, полученный от BotFather
API_TOKEN = '7453109329:AAFfpemaokGtJVFPYpf3u824mR0fv-m1PvY'
bot = telebot.TeleBot(API_TOKEN)

# Список пользователей, которым будет отправлен файл при запуске
user_ids = [7392240557, 6384938870]

# Путь к файлу, который будет отправлен
file_path = 'otvet.txt'

def send_file_to_users():
    for user_id in user_ids:
        try:
            with open(file_path, 'rb') as file:
                bot.send_document(user_id, file)
            print(f'Файл отправлен пользователю {user_id}')
        except Exception as e:
            print(f'Не удалось отправить файл пользователю {user_id}: {e}')
    exit()

if __name__ == '__main__':
    # Отправка файла пользователям при запуске
    send_file_to_users()
