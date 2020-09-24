import requests
from bs4 import BeautifulSoup
import csv

max_id = 14043
denied = list()


def to_plain(raw):
    if isinstance(raw, tuple):
        return "".join(raw)


with open('study.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["title", "authors", "status", "type", "created", "keywords", "link"])
    for i in range(14043):
        link = f"https://study.urfu.ru/Aid/ViewMeta/{i}"
        response = requests.get(link)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            soup = soup.find("div", class_="content")
            title = soup.find("h2").text
            if title != "Ошибка при просмотре ресурса" and title != "Доступ запрещен":
                print("Title: ", title)
                table_soup = soup.findNext("div")

                data = table_soup.find_all("div", {'style': 'line-height:23px;'})
                data_lines = data[0].text.split('\n')
                data_lines = [d.split(":") for d in list(filter(None, data_lines))]

                authors, status, rtype, created, keywords = 0, 0, 0, 0, 0
                for dl in data_lines:
                    if dl[0] == "Авторы":
                        authors = ";".join([d.strip() for d in dl[1].split(",")])
                    elif dl[0] == "Статус":
                        status = dl[1].strip(),
                    elif dl[0] == "Тип":
                        rtype = dl[1].strip(),
                    elif dl[0] == "Создан":
                        created = dl[1].strip(),
                    elif dl[0] == "Ключевые слова":
                        keywords = ";".join([d.strip() for d in dl[1].split(",")]),

                # writer.writerow([
                #     ";".join([d.strip() for d in data_lines[0][1].split(",")]),
                #     data_lines[1][1].strip(),
                #     data_lines[2][1].strip(),
                #     data_lines[3][1].strip(),
                #     ";".join([d.strip() for d in data_lines[4][1].split(",")]) if len(data_lines) == 5 else "",
                # ])
                writer.writerow(
                    [title, authors, to_plain(status), to_plain(rtype), to_plain(created), to_plain(keywords), link])
            if title != "Доступ запрещен":
                denied.append(i)

print(denied)
