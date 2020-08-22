import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import random

csv_file = open('MLibre discounts.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product', 'Old price', 'Discount', 'Actual Price'])

for page in range(1, 3):
    r = requests.get('https://www.mercadolibre.com.ar/ofertas?cat=MLA1000#origin=qcat&filter_applied=category_id&filter_position=' + str(page))
    soup = BeautifulSoup(r.content, 'lxml')
    sleep(random.randint(2, 10))
    for article in soup.find_all('div', class_='promotion-item__container'):
        p1 = article.find('div', class_='promotion-item__description')
        p2 = p1.find('div', class_='promotion-item__price-block')
        price = p2.find('span', class_='promotion-item__price').text
        item = p1.find('p', class_='promotion-item__title').text
        try:
            old_price = p1.find('span', class_='promotion-item__oldprice').text
            disc = p2.find('div', class_='promotion-item__price-additional-info')
            discount = disc.find('span', class_='promotion-item__discount').text

        except Exception as e:
            old_price = None
            discount = None
        if discount is not None:
            csv_writer.writerow([item, old_price, discount, price])

csv_file.close()







