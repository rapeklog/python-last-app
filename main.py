import requests

# Функция для получения IP без прокси
def get_ip_without_proxy():
    try:
        response = requests.get('https://icanhazip.com/')
        if response.status_code == 200:
            return response.text.strip()
    except requests.RequestException as e:
        print(f"Ошибка при запросе без прокси: {e}")
    return None

# Функция для проверки прокси
def check_proxy(proxy, protocol):
    try:
        proxies = {
            protocol: f"{protocol}://{proxy}"
        }
        response = requests.get(f"{protocol}://icanhazip.com/", proxies=proxies, timeout=10)
        if response.status_code == 200:
            return response.text.strip()
    except requests.RequestException:
        pass
    return None

# Чтение списка прокси из файла
def read_proxies_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

# Запись рабочей прокси в файл
def write_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')

def main():
    # Получаем IP без прокси
    ip_without_proxy = get_ip_without_proxy()
    if ip_without_proxy:
        print(f"IP без прокси: {ip_without_proxy}")
    else:
        print("Не удалось получить IP без прокси")
        return

    # Чтение списка прокси из файла proxy.txt
    proxies = read_proxies_from_file('proxy.txt')

    for proxy in proxies:
        # Проверка прокси на HTTP
        ip_http = check_proxy(proxy, 'http')
        if ip_http:
            print(f"HTTP прокси рабочий: {proxy}, IP: {ip_http}")
            write_to_file('http.txt', proxy)

            # Проверка прокси на HTTPS
            ip_https = check_proxy(proxy, 'https')
            if ip_https:
                print(f"HTTPS прокси рабочий: {proxy}, IP: {ip_https}")
                write_to_file('https.txt', proxy)
            else:
                print(f"HTTPS прокси не рабочий: {proxy}")
        else:
            print(f"HTTP прокси не рабочий: {proxy}")

if __name__ == "__main__":
    main()
