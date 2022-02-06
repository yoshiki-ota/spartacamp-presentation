import time
import requests
from bs4 import BeautifulSoup
import re


def main():
    pass


# キーワード取得
keyword = input("通知してほしい情報を入力してください：")

# トップページ情報取得
URL = "https://www.soccer-king.jp/"
# 情報格納
rest = requests.get(URL)
# BeautifulSoupにページ内容を読み込ませる
soup = BeautifulSoup(rest.text, 'lxml')

# タイトル＆リンク作成
for x in soup.find_all(class_=re.compile('tit')):
    print(x)
    # title_text = x.get_text()
    # title_url = x.attrs['href']
    # print(f"title: {title_text}, link: {title_url}")

if __name__ == '__main__':
    main()

if __name__ == '__main__':
    main()
