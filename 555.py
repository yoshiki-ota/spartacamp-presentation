import datetime
import time
import requests
from bs4 import BeautifulSoup
import re


def send_line_notify(notification_message):
    # LINE通知
    line_notify_token = 'Ej4smTf5zsot6FRgZm3WeMMd7T2AoL7tCGNLZYmCvU3'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'{notification_message}'}
    requests.post(line_notify_api, headers=headers, data=data)


def job():
    today_dummy = datetime.date.today()
    today = today_dummy.strftime('%Y%m%d')

    URL = "https://www.soccer-king.jp/"  # トップページ情報取得
    rest = requests.get(URL)  # 情報格納
    soup = BeautifulSoup(rest.text, 'lxml')  # BeautifulSoupを用いてlxmlで解析

    for today_info1 in soup.find_all(href=re.compile(today)):
        time.sleep(1)
        for today_info2 in today_info1.find_all(text=re.compile('(レネガス|川崎)')):
            title = today_info2
            url = today_info1.attrs['href']
            send_line_notify(title)
            send_line_notify(url)


"""
def job():
    # トップページ情報取得
    URL = "https://www.soccer-king.jp/"
    # 情報格納
    rest = requests.get(URL)
    # BeautifulSoupを用いてlxmlで解析
    soup = BeautifulSoup(rest.text, 'lxml')
    for x in soup.find_all(href=re.compile("20220208")):
        title_text = x.find_all('p', class_='tit')
        title_url = x.attrs['href']
        send_line_notify(title_text)
        send_line_notify(title_url)
"""


def main():
    job()
    # #sleep(1)で1秒間隔を置き負荷を軽減
    time.sleep(1)


if __name__ == '__main__':
    main()
