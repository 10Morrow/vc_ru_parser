import requests
from bs4 import BeautifulSoup


def get_category_data(url: str, mode: int) -> list:
    """парсит страницу с данными о категориях"""
    result_data_list = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    body = soup.find('body')
    mid = body.find('div', class_='layout__content l-relative')
    page_wraper = mid.find(id='page_wrapper')
    subsites_catalog = page_wraper.find('div', class_='subsites_catalog')
    catalog = subsites_catalog.find('div', class_='subsites_catalog__content')
    subscribed = catalog.find('div', class_='subsites_catalog__subscribed')
    recommended = catalog.find('div', class_='subsites_catalog__recommended')

    if mode == 0:
        catalog_list = subscribed
    else:
        catalog_list = recommended

    data_list = catalog_list.find_all('div', class_='subsites_catalog_item')
    for data in data_list:
        if mode == 0:
            a = data.find('a', class_='subsite_card_simple_short__title')
            result_data_list.append([a['href'], a.text.strip()])
        else:
            a = data.find('a', class_='subsite_card_simple__title')
            result_data_list.append([a['href'], a.text.strip()])

    return result_data_list