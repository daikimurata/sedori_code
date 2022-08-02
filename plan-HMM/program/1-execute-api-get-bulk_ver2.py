#coding:utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
OKBLUE  = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
ENDC    = '\033[0m'
UNDERLINE = '\033[4m'

import time
import sys
import os
import random
import requests
from datetime import datetime
from selenium import webdriver
# Selectタグが扱えるエレメントに変化させる為の関数を呼び出す
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# 操作する値を定義
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
flag = 0
output_rows = []
#ターゲットとなるECサイト・商品一覧１ページ目のURL
URL = 'https://shop.faber-hobby.jp/products/list.php?name=SALE1&disp_number=52&isStock=yes'


# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# Chromeを起動しWebページを開く部分
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# Chromeの起動
b = webdriver.Chrome('./chromedriver')
# 起動したChromeでURLを開く
b.get(URL)
#1秒間のスリープ
time.sleep(1)

# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# 開いたウェブから、情報を取り出す部分
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
while True:
    # ウェブから商品の名前とURLを取り出す
    classes = b.find_elements_by_class_name('itemname')
    
    # 商品数をコンソールに表示
    print(len(classes))
    
    # CSVに出力する文字列を作る
    for i in list(classes):
        a = i.find_elements_by_css_selector("a")
        name = str(a[0].text.replace(',',''))
        url  = str(a[0].get_attribute("href"))
        print(OKBLUE+UNDERLINE+url+ENDC)
        print(name)
        # 配列にCSVファイルに出力する用の文字列を格納
        output_rows.append('{ITEM_NAME},{URL}'.format(ITEM_NAME=name,URL=url))

    q = b.find_element_by_class_name('navi')
    a = q.find_elements_by_css_selector("a")
    for i in a:
        name = str(i.text)
        url  = str(i.get_attribute("href"))
        if name == '次へ>>':
            flag = 1
            i.click()
        else:
            flag = 0
    if flag ==0:
        break
    else:
        time.sleep(1)
        continue

# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# 情報をファイルに書き込む部分
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# 上書きモード
with open('out.csv','w', encoding='utf-8') as f:
    # 配列の要素をファイルに書き込み
    for output_row in output_rows:
        print(output_row, file=f)
f.close()
