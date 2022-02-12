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
infomation = soup.find_all(href=re.compile(today))


def i():
    for today_info1 in soup.find_all(href=re.compile(today)):
        for today_info2 in today_info1.find_all(text=re.compile('(江坂|優勝)')):
            title = today_info2
            url = today_info1.attrs['href']
            # msg = f"[TITLE]:{title},[URL]: {url}"
            # return [title, url]
            list = [title, url]
            result = '\n'.join(list)
            return result


def x(word):
    today_dummy = datetime.date.today()
    today = today_dummy.strftime('%Y%m%d')

    URL = "https://www.soccer-king.jp/"  # トップページ情報取得
    rest = requests.get(URL)  # 情報格納
    soup = BeautifulSoup(rest.text, 'lxml')  # BeautifulSoupを用いてlxmlで解析
    infomation = soup.find_all(href=re.compile(today))
    count = 0
    list = []

    for topic in infomation:
        if topic.contents[0].find(word) > -1:
            list.append(topic.contents[0])
            list.append(topic.get('href'))
            count += 1
    if count == 0:
        list.append("記事が見つかりませんでした！！")

    result = '\n'.join(list)
    return result


if __name__ == '__main__':
    # i()
    x()
