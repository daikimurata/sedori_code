#coding:utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
OKBLUE  = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
ENDC    = '\033[0m'
from amazon.api import AmazonAPI
from amazon.api import LookupException, AsinNotFound
from time import sleep
import codecs
import re
import requests
import shutil
import csv
import method
import os

ACCESS_KEY = "ここにACCESS_KEYを入れます"
SECRET_ACCESS_KEY = "ここにSEACRET_ACCESS_KEYを入れます"
ASSOCIATE_TAG = "ASSOCIATE_TAGを入れます"
error = 0



# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# 画像を読み込む関数
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
def download_img(url, file_name):
    # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
    # 引数:画像のURL、画像ファイルの名前
    # 
    # 戻り値:なし
    # 
    # 用途:引数のURLから画像ファイルを読み込んで引数のファイル名
    # で保存する関数
    # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(os.path.join('image',file_name), 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)



# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# out.csvから読み込んだ内容を抽出してout2.csvに情報を書き込む
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
def amazon_api(JAN,name,price,url,counter):
    # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
    # 引数:JANコード、商品名、価格、商品情報のURL、counter?
    # 
    # 戻り値:なし
    # 
    # 用途:
    # ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
    # Amazon APIへの接続前のプロキシ確認（ログイン的なやつ）
    amazon = AmazonAPI(ACCESS_KEY, SECRET_ACCESS_KEY, ASSOCIATE_TAG, region="JP")
    
    try:
        # 商品情報の取得
        product = amazon.lookup(ItemId=JAN, IdType="EAN", SearchIndex="All")
        # Amazonの中に商品情報があるかどうかを判定
        if isinstance(product, list):
            print('NO amazon')
        else:
            # 商品情報を移し替えて表示する
            asin = product.asin
            title= product.title
            amazon_price= product.price_and_currency[0]
            group = product.product_group
            rank  = product.sales_rank
            if amazon_price is None:
                amazon_price = 0
            reviews = product.reviews[1]
            print('ASIN: '+ OKBLUE +str(asin) + ENDC)
            print(title)
            print('price: '+str(amazon_price))
            print('group: '+str(group))
            print('ranking: '+str(rank))

            image_url = 'http://images-jp.amazon.com/images/P/'+asin+'.09.THUMBZZZ.jpg'
            image_name = asin + '.jpg'
            #download_img(image_url, image_name)


# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# 手数料の計算部分
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# ===============================================================================================================================
            # 改良の余地あり
            mono_url = 'http://mnrate.com/item/aid/'+ asin
            dif = int(price) - int(amazon_price)
            # 手数料（FBAの固定費＋差額）
            r_dif = int(amazon_price)*0.1 + int(dif)
            # 利益率の計算
            br = - r_dif/int(price)*100
            print('BR: ' + PURPLE + str(int(br)) +ENDC)
            amazon_url = 'https://www.amazon.co.jp/s/ref=nb_sb_noss?__mk_ja_JP=カタカナ&url=search-alias%3Daps&field-keywords=' + JAN
            #save(JAN,asin,mono_url,price,amazon_price,dif,r_dif,br,url,amazon_url,group,rank)
            strings = str(JAN)+','+str(asin)+','+str(mono_url)+','+str(name)+','+str(price)+','+str(amazon_price)+','+str(dif)+','+str(int(r_dif))+','+str(br)+','+str(url)+','+str(amazon_url)+','+str(group)+','+str(rank)+'\n'
            b.write(strings)
# ===============================================================================================================================

    except Exception as e:
        #print(e)
        if 'ASIN(s) not found:' in e:
            counter = 7
            print ('ASIN(s) not found:')
        counter = counter +1
        if counter > 1:
            print ('Not found')
        else:
            sleep(0.5)
            amazon_api(JAN,name,price,url,counter)

JAN = 0
count = -1
# CSVファイルの読み込み
a = open('out2.csv','r')
b = open('out3.csv','w')
# csvファイルのヘッダーの書き込み
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# ヘッダー内容
# JANコード
# ASINコード(Amazonで使われてる商品ID?)
# モノレートのURL
# 商品名
# ECサイトの値段
# Amazonの値段
# AmazonとECサイトの差額
# 手数料
# 利益率
# 仕入れ先のURL
# AmazonのURL
# Amazonの商品グループ
# Amazonの売上ランキング
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
b.write('JAN,ASIN,MONO,NAME,PRICE,amazon_PRICE,DIF,R_DIF,BR,URL,amazonURL,Category,Ranking\n')
# 2番のコードのcsvファイルから読み取り、APIの実行
for line in a:
    count = count + 1
    LINE = line.rstrip().split(',')
    JAN   = LINE[0]
    name  = LINE[1]
    price = LINE[2]
    url   = LINE[3]
    counter = 0
    print ('\n\n')
    # ヘッダーを避けている
    if count >= 1:
        print (OKGREEN + str(count) + ENDC)
        print ('JAN: '+str(JAN))
        amazon_api(JAN,name,price,url,counter)
        sleep(0.3)

a.close()
b.close()
