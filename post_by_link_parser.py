import requests
from bs4 import BeautifulSoup
import time


def _text_handler(data):
    """функция обработки текста, чтобы в итоге оставить лишь чистый текст с именем тега"""
    if data.name in ["h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "b", "li"]:
        if data.text:
            return [(data.text.strip(), data.name)]
        else:
            return []
    else:
        result = []
        data_parts = data.find_all(lambda tag: tag.parent == data)
        for block in data_parts:
            result += _text_handler(block)
        return result


def get_post_data(article_url):
    """парсит страницу статьи, с целью собрать весь текст"""
    result_data_list = []
    time.sleep(5)
    response = requests.get(article_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    page_wrapper = soup.find(id='page_wrapper')
    page = page_wrapper.find('div', class_='page page--entry')
    article = page.find('div', class_='l-entry')
    article_header = article.find('h1', class_='content-title').text.strip()
    article_body = article.find('div', class_='l-entry__content')
    finished_artcile_body = article_body.find('div', class_='content--full')
    tags = finished_artcile_body.find_all(lambda tag: tag.parent == finished_artcile_body and
                                                      'figure-image' not in tag.get('class', []))
    result_data_list +=[("h1", article_header)]
    for i in tags:
        result_data_list += _text_handler(i)

    return result_data_list

