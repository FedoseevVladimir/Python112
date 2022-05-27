# ============================================================
# HomeWork на 18.05.2022
# import csv
#
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def write_csv(data):
#     with open('data2.csv', 'a', encoding="utf-8") as f:
#         writer = csv.writer(f, delimiter=";", lineterminator='\r')
#         writer.writerow((data['name'],
#                          data['description'],
#                          data['price']
#                          ))
#
#
# def get_page_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#
#     elements = soup.find_all('a', class_="css-5l099z ewrty961")
#     for elem in elements:
#         name = elem.find('div', class_="css-17lk78h e3f4v4l2").text
#         des = elem.find('div', class_="css-1fe6w6s e162wx9x0").text
#         price = elem.find('div', class_="css-1dv8s3l eyvqki91").text
#
#         data = {
#             'name': name,
#             'description': des,
#             'price': price
#         }
#
#         write_csv(data)
#
#
# def main():
#     url = 'https://auto.drom.ru/toyota/camry/generation7/restyling0/'
#     get_page_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()
# ========================================================================