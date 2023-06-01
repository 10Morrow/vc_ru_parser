import re
from main_page_parser import get_links_list
from post_by_link_parser import get_post_data
from write_data import write_data_in_csv
from parse_more_data import get_new_data


def main():
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

    links = list(set(links))

    for article_link in links:
        pass
        # article_data = get_post_data(article_url=article_link)
        # print(article_data)
        # print(write_data_in_csv(data=article_data, article_link=article_link))

    print(len(links), len(set(links)))


if __name__ == "__main__":
    main()
