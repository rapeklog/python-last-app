import telebot
import time

# Здесь вставьте ваш токен, полученный от BotFather
API_TOKEN = '7465039625:AAGifYhJxNtYZTQCb-mxC4Vs_5MYMhDUmbU'
bot = telebot.TeleBot(API_TOKEN)

# Список пользователей, которым будет отправлен файл при запуске
user_ids = [7392240557, 6384938870]

def send_file_to_users():
    for user_id in user_ids:
        try:
            with open("http.txt", 'rb') as file:
                bot.send_document(user_id, file)
            print(f'Файл отправлен пользователю {user_id}')
            with open("https.txt", 'rb') as file:
                bot.send_document(user_id, file)
        except Exception as e:
            print(f'Не удалось отправить файл пользователю {user_id}: {e}')
    exit()

if __name__ == '__main__':
    # Отправка файла пользователям при запуске
    send_file_to_users()
