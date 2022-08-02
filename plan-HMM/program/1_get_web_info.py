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
import method_interface
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# 操作する値を定義
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
#ターゲットとなるECサイト・商品一覧１ページ目のURL
URL = 'https://shop.faber-hobby.jp/products/list.php?name=SALE1&disp_number=52&isStock=yes'
# 出力ファイルの名前
FILE_NAME = 'out.csv'

# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# 実行部分
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
if __name__ == '__main__':
    print('ツールを実行します')
    method_interface.write_new_file(
        FILE_NAME,
        method_interface.create_output_rows(
            method_interface.get_chrome_web_info(URL)
            )
        )
    print('ツールを終了します')
    