import re
from main_page_parser import get_links_list
from post_by_link_parser import get_post_data
from write_data import write_data_in_csv
from parse_more_data import get_new_data
from parse_category_list import get_category_data


def main():
    """Главная функция запускающая весь код."""
    common_list = get_category_data("https://vc.ru/subs", 0)
    recommended_list = get_category_data("https://vc.ru/subs", 1)
    mode = int(input(f"Выберите список категорий:\n1. Общий. (размер: {len(common_list)})\n2. рекомендовано. (размер: {len(recommended_list)})\nвведите цифру: "))
    if mode == 1:
        category_list = common_list
    else:
        category_list = recommended_list
    for i, category in enumerate(category_list):
        print(f"{i}. {category[-1]}")
    choosen_category = category_list[int(input("Выберите категорию. Введите цифру: "))]
    print(f"выбранная категория: '{choosen_category[-1]}'")
    article_ids = []
    url = "https://vc.ru"
    links = get_links_list(url=url)
    for link in links:
        match = re.search(r'/(\d+)-', link)
        if match:
            article_id = int(match.group(1))
            article_ids.append(article_id)
    last_id = article_ids[-1]
    last_sorting_value = ''
    for i in range(2, 11):
        if last_sorting_value:
            link = f"https://vc.ru/popular/more?last_id={last_id}&page={i}" \
                   f"&exclude_lids={article_ids}&last_sorting_value={last_sorting_value}&mode=raw"
        else:
            link = f"https://vc.ru/popular/more?last_id={last_id}&page={i}&exclude_lids={article_ids}&mode=raw"
        new_data = get_new_data(link)
        links += new_data[-1]
        last_id = new_data[0]
        article_ids = new_data[1]
        last_sorting_value = new_data[2]

    chosen_links_list = [link for link in links if link.startswith(choosen_category[0])]

    for article_link in chosen_links_list:
        pass
        article_data = get_post_data(article_url=article_link)
        print(article_data)
        print(write_data_in_csv(data=article_data, article_link=article_link))


if __name__ == "__main__":
    main()
