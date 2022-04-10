import requests  # Импорт библиотеки Requests
from bs4 import BeautifulSoup  # Импорт библиотеки Beautiful Soup


# Основная функция
def main():
    # URL страницы
    url = 'https://stopgame.ru/news/all/p1'
    # Получаем страницу
    r = requests.get(url)
    # Открываем файл
    with open('test.html', 'w', encoding='utf-8') as output_file:
        # Добавляем страницу для парсинга
        soup = BeautifulSoup(r.text, 'html.parser')
        # Получаем все по селектору элементы и проходима по ним циклам
        for i in soup.select(".items > .article-summary > .article-description"):
            # Получаем заголовок
            title = i.select(".caption > a[href]")
            # Добавляем заголовок во файл
            output_file.writelines("<h2>" + title[0].text + "</h2>")


# Запуск кода
if __name__ == '__main__':
    main()