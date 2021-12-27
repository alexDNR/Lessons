import requests
from bs4 import BeautifulSoup
import csv
import time

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 YaBrowser/21.6.4.694 Yowser/2.5 Safari/537.36', 'accept': '*/*'}
FILE = 'cars.csv'

def get_html(url, params=None):
    r = requests.get(url, headers = HEADERS, params = params)
    return r

def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find('div', class_='paging')
    if pagination:  
        page_count = int(pagination.get_text(strip=True).replace('Вперед1 / ', ''))
    else:
        page_count = 1
    return page_count    
  

def get_content(html, rate):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_='item-thumb')
    cars = []
    for item in items:
        price_euro = item.find('div', class_='pricing-container').get_text(strip=True).replace(' ', '').replace('+налоги', '')
        price_ruble = price_euro.replace('€+налоги', '').replace('€', '')
        price_ruble = round(int(price_ruble) * rate)

        #опрееделние VIN кода - его наличие - НАЧАЛО
        vin = item.find('span', class_='item-label label-vin')
        if vin:
            vin = '+'
        else:
            vin = '-'  
        #опрееделние VIN кода - его наличие - ЗАКОНЧИЛИ

        info_item = item.find('div', class_='item-parameters').find_all('span')
        engine = info_item[0].text
        transmission = info_item[2].text
        mileage = info_item[3].text
        body = info_item[4].text

        cars.append({
            'year': item.find('div', class_='title-year').get_text(strip=True),
            'car': item.find('div', class_='line1').get_text(strip=True),
            'price_euro': price_euro,
            'price_ruble': price_ruble,
            'vin': vin,
            'engine': engine,
            'transmission': transmission,
            'mileage': mileage,
            'body': body,
            'link': item.get('href')
        })
    return cars

def save_file(items, path):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(['year', 'car', 'price_euro', 'price_ruble', 'vin', 'engine', 'transmission', 'mileage', 'body', 'link'])
        for item in items:
            writer.writerow([item['year'], item['car'], item['price_euro'], item['price_ruble'], item['vin'], item['engine'], item['transmission'], item['mileage'], item['body'], item['link']])

def parce():
    URL = input('Введите URL страницы интересующей марки авто с сайта autoplius.lt: ')
    URL = URL.strip()
    rate = float(input('Введите курс рубля к евро = '))
    html = get_html(URL)
    print ('Status code =', html.status_code)
    if html.status_code == 200:
        cars = []
        pages = get_pages_count(html.text)
        for i in range(1, int(pages) + 1):
            print(f'Parse page count {i} in {pages}...')
            html = get_html(URL, params = {'page': i}) # переход по каждой странице через функцию
            cars.extend(get_content(html.text, rate)) # дополяем пустой массив карточками с каждой страницы   
            time.sleep(1)
        print(f'Получено {len(cars)} автомобилей') # выводим количество автомобилей
        save_file(cars, FILE)
    else:
        print('Error html')    

parce()
