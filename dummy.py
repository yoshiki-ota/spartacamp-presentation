import datetime
import keyword
import time
import requests
from bs4 import BeautifulSoup
import re

today_dummy = datetime.date.today()
today = today_dummy.strftime('%Y%m%d')

URL = "https://www.soccer-king.jp/"  # トップページ情報取得
rest = requests.get(URL)  # 情報格納
soup = BeautifulSoup(rest.text, 'lxml')  # BeautifulSoupを用いてlxmlで解析
for today_info1 in soup.find_all('li'):
    for today_info2 in today_info1.find_all('href'):
        print(today_info2)
    print(today_info1)
# def i():
#     list = []today_info1 in soup.find_all(href=re.compile(today)):
#     for
#         for today_info2 in today_info1.find_all(text=re.compile('(ナポリ|ベイル)')):
#             title = today_info2
#             url = today_info1.attrs['href']
#             list = [title, url]
#             result = '\n'.join(list)
#             print(result)
#
#
# if __name__ == '__main__':
#     i()
