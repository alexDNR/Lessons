import requests
from bs4 import BeautifulSoup
import csv

URL = "https://auto.ria.com/ru/newauto/marka-bmw/"
HEADERS = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 YaBrowser/21.6.4.694 Yowser/2.5 Safari/537.36', 'accept': '*/*'}
HOST = 'https://auto.ria.com'
FILE = 'cars.csv'


def get_html(url, params=None):
    r = requests.get(url, headers = HEADERS, params = params)
    return r

# парсер количества страниц с автомобилями
def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')   
    paginations = soup.find_all('span', class_='mhide') # находим все вкладки с авто
    if paginations:
        return int(paginations[-1].get_text()) # делаем срез и показываем только последнее значение - то есть сколько всего у нас страниц получается
    else:
        return 1    

# функция которая будет принимать html с которой будет работать 
def get_content(html):
    suop = BeautifulSoup(html, 'html.parser') 
    items = suop.find_all('section', class_='proposition') # вот тут указываем элемент из DOM дерева, в котором лежат все данные об автомобиле, а также его тег 

    cars = [] # пустой массив, в который будем записывать данные об автомобилях
    for item in items:
        price_ruble = item.find('span', class_='size16')
        if price_ruble:
            price_ruble = item.find('span', class_='size16').get_text().replace(' грн', '').replace(' $', '').replace(' ', '') # убираем лишние пробелы и валюту гривны
            price_ruble = f'{int(price_ruble) * 2.73}₽' # переделываем гривны в рубли
        else:
            price_ruble = 'Цены в рублях нет'
        
        cars.append({
            'car': item.find('span', class_='link').get_text(strip=True), # вот тут указываем тег, который надо найти и его класс. Получаем список заголовоков каждого объявленияget.text() в данном случае метод библиотеки bs4. strip=True - удаляет лишние концевые пробелы (начало и конец строки)
            'link': HOST + item.find('a', class_='proposition_link').get('href'),
            'price_dollar': item.find('span', class_='green').get_text(strip=True).replace(' ', ''),
            'price_ruble': price_ruble,
            #'info': item.find('div', class_='proposition_information').get_text(strip=True).replace(' • ', ' ')
        })
    return cars

def save_file(items, path): # функция сохранения файлв в формате CSV - которая принимает элементы из get_content и путь сохранения файла
    with open(path, 'w', newline='', encoding="utf-8") as file: # открываем файл (если его нет, то он создаётся) с функцией 'w' - write 
        writer = csv.writer(file, delimiter='\t') # разделитель тут ";"
        writer.writerow(['car', 'link', 'price_$', 'price_rub']) # создаём строку с заголовками стообцов
        for item in items:
            writer.writerow([item['car'], item['link'], item['price_dollar'], item['price_ruble']]) # записываем каждое поле в столбец


def parse():
    html = get_html(URL)
    print("Status code:", html.status_code)
    if html.status_code == 200:
        cars = []
        pages_count = get_pages_count(html.text) # получаем количество страниц
        for page in range(1, pages_count + 1): # запускаем цикл по количеству страниц, чтобы получить все карточки автомобилей
            print(f'Парсинг страницы {page} из {pages_count}...') 
            html = get_html(URL, params = {'page': page}) # переход по каждой странице через функцию
            cars.extend(get_content(html.text)) # дополяем пустой массив карточками с каждой страницы   
        print(f'Получено {len(cars)} автомобилей') # выводим количество автомобилей
        save_file(cars, FILE) 
    else:
        print("Error html")

parse()

