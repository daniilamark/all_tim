# pip install requests
# pip install beautifulsoup4


import requests  # Импортируем библиотек Requests


# Основная функция
def main():
    # URL страницы
    url = 'https://stopgame.ru/'
    # Получаем страницу
    r = requests.get(url)
    # Открываем файл
    with open('test.html', 'w', encoding='utf-8') as output_file:
        # Выводим страницу в HTML файл
        output_file.write(r.text)


# Запуск кода
if __name__ == '__main__':
    main()