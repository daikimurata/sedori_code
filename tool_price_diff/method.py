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
#ターゲットとなるECサイト・商品一覧１ページ目のURL
URL = 'https://shop.faber-hobby.jp/products/list.php?name=SALE1&disp_number=52&isStock=yes'
# 出力ファイルの名前
FILE_NAME = 'out.csv'

# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# Chromeを起動しWebページを開く部分
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
def get_chrome_web_info(url:str, webdriver = './chromedriver') -> webdriver:
    # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
    # 引数:情報取得するwebページのurl、
    #     　webドライバーの選択(任意)
    # 
    # 戻り値:WebDriver型のwebページの情報
    # 
    # 用途:引数のurlが表す対象から情報を取得する
    # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
    # Chromeの起動
    b = webdriver.Chrome(webdriver)
    # 起動したChromeでURLを開く
    b.get(url)
    #1秒間のスリープ
    time.sleep(1)
    return b

# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# 開いたウェブから、情報を取り出す部分(ウェブによって改変する必要あり)
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
def create_output_rows(b:webdriver) -> list:
    # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
    # 引数:webの情報を持ったwebdriver型のオブジェクト
    # 
    # 戻り値:csvファイルに出力される文字列型の要素のリスト
    # 
    # 用途:webの情報からcsvファイルに書き込むための文字列リストを
    #     作成する
    # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
    output_rows = []
    flag = 0
    while True:
        classes = b.find_elements_by_class_name('itemname')
        print(len(classes))
        for i in list(classes):
            a = i.find_elements_by_css_selector("a")
            name = str(a[0].text.replace(',',''))
            url  = str(a[0].get_attribute("href"))
            print(OKBLUE+UNDERLINE+url+ENDC)
            print(name)
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
    return output_rows

# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# 情報をファイルに書き込むメソッド
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
def write_new_file(file_name:str,output_rows:list,header:str=None):
    # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
    # 引数:書き込むファイルの相対パスと名前,書きこむリスト、
    #      csvファイルのヘッダー（設定が必要な場合）
    # 
    # 戻り値:なし
    # 
    # 用途:文字列の入ったリストの要素を一つずつ取り出して書きこむ
    #      対象のファイルに書き込む
    # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
    print('{}に書き込みます'.format(file_name))
    # 上書きモード
    with open(file_name,'w', encoding='utf-8') as f:
        if header is not None:
            print(header, file=f)
        # 配列の要素をファイルに書き込み
        for output_row in output_rows:
            print(output_row, file=f)
    f.close()

# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# 情報をファイルに読み込んでリストにして返すメソッド
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
def open_csv_file_list(file_name:str):
    # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
    # 引数:読み込みたいcsvファイルの相対パス
    # 
    # 戻り値:csvファイルの各行が文字列型の要素となったリスト
    # 
    # 用途:csvファイル内のデータを文字列型のリストにして返す
    # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
    read_csv_list = open(file_name,'r')
    return read_csv_list