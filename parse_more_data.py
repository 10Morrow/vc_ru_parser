import requests
import json
from bs4 import BeautifulSoup


def get_new_data(url: str) -> list:
    """парсит данные автоматически подгружаемые данные."""
    links_list = []
    response = requests.get(url)
    json_data = json.loads(response.content)
    last_id = json_data["data"]["last_id"]
    exclude_id_list = json_data["data"]["exclude_ids"]
    html_document = json_data["data"]["items_html"]
    last_sorting_value = json_data["data"]["last_sorting_value"]
    clear_html_data = html_document.replace("\n", "")
    soup = BeautifulSoup(clear_html_data, 'html.parser')
    posts = soup.find_all('div', class_='feed__item l-island-round')
    for post in posts:
        link = post.find('a', class_='content-link')['href']
        links_list.append(link)
    return [last_id, exclude_id_list, last_sorting_value, links_list]
