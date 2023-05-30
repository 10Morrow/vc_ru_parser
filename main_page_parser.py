import requests
from bs4 import BeautifulSoup


def get_links_list(url):
    """парсит веб-сайт чтобы собрать список ссылок на статьи."""
    links_list = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    body = soup.find('body')
    feed_container = body.find('div', class_='feed__container')
    feeds_chunk = feed_container.find('div', class_='feed__chunk')
    posts = feeds_chunk.find_all(class_='feed__item l-island-round')
    for post in posts:
        link = post.find('a', class_='content-link')['href']
        links_list.append(link)
    return links_list