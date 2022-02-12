import datetime
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
        for today_info2 in today_info1.find_all(text=re.compile('(ナポリ|スターリング)')):
            title = today_info2
            url = today_info1.attrs['href']
            list = [title, url]
            # list.append(title)
            # list.append(url)
            result = '\n'.join(list)
            # return result
            print(result)


def o(word):
    count = 0
    list = []

    for today_info1 in soup.find_all(href=re.compile(today)):
        if today_info1.contents[0].find(word) > -1:
            list.append(today_info1.contents[0])
            list.append(today_info1.get('href'))
            count += 1
        if count == 0:
            list.append("記事が見つかりませんでした！！")

        result = '\n'.join(list)
        print(result)

        # return result


if __name__ == '__main__':
    # i()
    o()
