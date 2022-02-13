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


def i():
    list = []
    for today_info1 in soup.find_all(href=re.compile(today)):
        for today_info2 in today_info1.find_all(text=re.compile('(チェルシー|おおおお)')):
            title = today_info2
            url = today_info1.attrs['href']
            list = [title, url]
            # list.append(title)
            # list.append(url)
            result = '\n'.join(list)
            return result
            # print(result)


# def o():　試した１
#     count = 0
#     list = []
#     word = "チェルシー"
#     for today_info1 in soup.find_all(href=re.compile(today)):
#         if today_info1.contents[0].find(word) > -1:
#             list.append(today_info1.contents[0])
#             list.append(today_info1.get('href'))
#             count += 1
#     if count == 0:
#         list.append("お探しの記事が見つかりませんでした")
#
#         result = '\n'.join(list)
#         print(result)
#         # return result
#
#
# def r():　　試した２
#     count = 0
#     list = []
#     word = "優勝"
#     # スクレイピング結果から引数wordを含む記事を結果リストに格納
#     for topic in topics:
#         if topic.contents[0].find(word) > -1:
#             list.append(topic.contents[0])
#             list.append(topic.get('href'))
#             count += 1
#     if count == 0:
#         list.append("該当記事はありません")
#
#     # リスト内の要素間に改行を挿入して返却
#     result = '\n'.join(list)
#     return result
#

if __name__ == '__main__':
    i()
    # o()
    # r()
