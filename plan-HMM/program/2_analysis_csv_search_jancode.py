#coding:utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
OKBLUE  = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
ENDC    = '\033[0m'

import requests
from time import sleep
import method

OPEN_FILE_NAME = 'out.csv'
WRITE_FILE_NAME='out2.csv'
output_rows =[]

a = open(OPEN_FILE_NAME,'r')
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# out.csvから読み込んだ内容を抽出してout2.csvに情報を書き込む
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
for i in a:
    LINE = i.rstrip().split(',')
    name = LINE[0]
    url  = LINE[1]
    r = requests.get(url)
    content = r.text
    try:
        price = content.split('<span id="price02_default" itemprop="price" content=\'')[1].split('\'')[0].replace(',','')
        print ('【Price】-->¥'+price)
        jan  = content.split('<dd itemprop="gtin13">')[1].split('</dd>')[0]
        print (OKGREEN+'【JAN】-->'+jan+ENDC)
        output_rows.append(jan+','+name+','+price+','+url+'\n')
    except:
        print ('Fault')
    sleep(1)
method.write_new_file(WRITE_FILE_NAME,output_rows)
a.close()

