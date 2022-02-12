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


def information():
    for today_info1 in soup.find_all(href=re.compile(today)):
        time.sleep(1)
        for today_info2 in today_info1.find_all(text=re.compile('(ミラン|川崎)')):
            title = today_info2
            url = today_info1.attrs['href']
            print(title)
            print(url)


"""　一応ベースは残しておく
soup = BeautifulSoup(rest.text, 'lxml')
time.sleep(1)
for x in soup.find_all(href=re.compile("20220211")):
    time.sleep(3)
    title_text = x.find_all('p', class_='tit')
    title_url = x.attrs['href']
    print(title_text)
    print(title_url)
"""


def main():
    information()
    time.sleep(1)


if __name__ == '__main__':
    main()
