from main_page_parser import get_links_list
from post_by_link_parser import get_post_data
from write_data import write_data_in_csv


def main():
    url = "https://vc.ru"
    links = get_links_list(url=url)
    for article_link in links:
        article_data = get_post_data(article_url=article_link)
        print(article_data)
        print(write_data_in_csv(data=article_data, article_link=article_link))


if __name__ == "__main__":
    main()