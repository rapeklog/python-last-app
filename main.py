import requests

a = requests.get("https://icanhazip.com/")

# Открываем файл otvet.txt в режиме записи
with open('otvet.txt', 'w') as file:
    # Записываем строку "test" в файл
    file.write(a.text)

print('Содержимое записано в otvet.txt')
