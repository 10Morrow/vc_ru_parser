import csv
import datetime


def write_data_in_csv(data, article_link):
    """создает .csv файл и записывает в него данные статьи"""
    current_time = datetime.datetime.now()
    filename = current_time.strftime("data/article_%Y-%m-%d_%H-%M-%S.csv")
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        print(article_link, data[0])
        first_line = (article_link,) + data[0]
        writer.writerow(first_line)
        for row in data[1:]:
            writer.writerow(('',) + row)

    return "данные успешно записаны"
