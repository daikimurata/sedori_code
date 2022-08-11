# coding: utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
OKBLUE  = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
ENDC    = '\033[0m'
import os
import csv
import sys
import codecs
# from urlparse import urllib #URL --> Domain
from time import sleep
import requests
import random
from operator import itemgetter #sort by factor

a = open('out3.csv','r')
# htmlファイルの作成
b = open(os.path.join('data','page.html'),'w')
# ===============================================================================================================================
#b.write('<meta name="viewport" content="initial-scale=0.7">')
b.write('<div class="all">')
b.write('<head>\n')
b.write('<meta charset="utf-8">\n')
b.write('<link rel="shortcut icon" href="fig/icon.png" type="image/vnd.microsoft.icon">\n')
b.write('<TITLE>せどりちゃんねる</TITLE>\n')
b.write('<link rel="stylesheet" type="text/css" href="css.css">\n')
b.write('<script src="Java.js"></script>\n')
b.write('</head>\n')
b.write('<audio id="sound-file" preload="auto">\n<source src="fig/line.mp3" type="audio/mp3">\n</audio>\n')



#b.write('<div class="zentai">\n')
#b.write('<div class="title">\n')
#b.write('<div class="photo-show">\n<a href="https://line.me/R/ti/p/%40dnn4495i"><img height="36" border="0" alt="友だち追加" src="https://scdn.line-apps.com/n/line_add_friends/btn/ja.png"></a>\n')
#b.write('<div class="photo-show">\n<img src="fig/nth-of-type(1).png" width="200" height="200">\n<img src="fig/nth-of-type(2).png" width="200" height="200">\n<img src="fig/nth-of-type(3).png" width="200" height="200">\n<img src="fig/nth-of-type(4).png" width="200" height="200">\n<img src="fig/nth-of-type(5).png" width="200" height="200">\n<img src="fig/nth-of-type(6).png" width="200" height="200">\n<img src="fig/nth-of-type(7).png" width="200" height="200">\n<img src="fig/nth-of-type(8).png" width="200" height="200">\n</div>\n')
#b.write('<div class="title">')
b.write('<div class="pic">\n\
<img src="fig/falcom_logo.png" width="200" align="middle" alt="">\n\
</div>')
#<div class="front_amazon">\n\
#<marquee behavior="alternate" loop="-1"><font size="20" color="green"><img src="fig/icon2.png" width="90" height="90">\n</marquee>\n</div></div>\n')

#b.write('<marquee><font color="white" face="Comic Sans MS" size="4">Developed by Shuto K in 2017.</marquee>\n')

b.write('<div class="TITLE"><img src="fig/sedori.png" width="400" align="middle" alt=""></div>\n')

b.write('<div class="LINE">\n\
<a href="https://line.me/R/ti/p/%40dnn4495i"><img height="25" border="0" alt="友だち追加" src="https://scdn.line-apps.com/n/line_add_friends/btn/ja.png" width="70"></a>\n\
</div>\n'
)

b.write('<div class="QR">\n\
<img src="http://qr-official.line.me/L/KkQXNkcwpf.png" width="70">\n\
</div>\n'
)

b.write('<div class="LINE_here"><font size="2" color="white" style="font-weight:bold">LINE@はこちら!!↑</font></div>\n')

#b.write('<p width=500px><font size="4" color="white" width=500>\n\
#<br>We collect informations from online stores and compare these with Amazon. \n\
#<br>DIF means defference of the price between the online store and Amazon. \n\
#<br>R_DIF means real difference excepted commission in the case of selling on Amazon. \n\
#<br>Beneficial rate, Benefit is calculated by dividing R_DIF with the price.\n\
#<br>The interface provide you with beneficial information to resell on Amazon market.\n')

#b.write('<marquee><img src="fig/icon.png" width="30" height="30"><font color="white" size="3">Welcome to SedoriChannel<img src="fig/icon.png" width="30" height="30">Here, We compare the price of many items between "Rakuten ichiba" and "Amazon" and show items, which you should procure as soon as posssible, by sorting its beneficial rate from large to small.</marquee>\n')
b.write('</div></p>\n')
# ===============================================================================================================================

# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# 有力商品の選定をする部分
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
out_list = []
count = 0
for line in a:
    count = count + 1
    # ヘッダーは飛ばす
    if count != 1:
        LINE = line.rstrip().split(',')
        count_list = len(LINE)
        # 要素13個あり、かつランキングに入ってるなら有力商品ってこと？
        # if count_list == 12 and LINE[12]!='None':
        #     LINE[12] = int(LINE[12])#change +- of Beneficial_rate to sort from small to large
        #     out_list.append(LINE)
        # 要素数12個（AmazonにもECサイトにも商品が存在する）＋利益率が0以上なら表示
        if count_list == 12 and LINE[7] > 0:
            LINE[7] = int(LINE[7])



# 利益率の高い順に並び替え
out_list.sort(key=itemgetter(7))
# ===============================================================================================================================
b.write('<body bgcolor="#003366">\n')
#b.write('<div style="width:1605px; border-style:solid;border-width:1px;">\n')
#b.write('<div style="height:700px; width:1700px; overflow-x:scroll; position:relative;">\n')
#b.write('<div style="height:700px; width:1700px; overflow-x:scroll; position: absolute; top: 330px; left: 50px;">\n')
b.write('<div style="height:900px; width:1400px; overflow-x:scroll; position: relative; top:10px; left:50px;">\n')
b.write('<table  border="5" cellspacing="0" bgcolor="white" width=1400 style="position: relative; top:0px; left:0px;">\n')
#b.write('<colgroup>\n\
#<col style="width:20px">\n\
#<col style="width:150px">\n\
#<col style="width:140px">\n\
#<col style="width:70px">\n\
#<col style="width:100px;>\n\
#<col style="width:400px">\n\
#<col style="width:120px">\n\
#<col style="width:120px">\n\
#<col style="width:80px">\n\
#<col style="width:80px">\n\
#<col style="width:85px">\n\
#<col style="width:60px">\n\
#<col style="width:60px">\n\
#<col style="width:100px">\n\
##<col style="width:100px">\n\
#</colgroup>\n')
b.write('<thead>\n')
b.write('<tr style="height:80px">\n')
b.write('<td align="center" bgcolor= "#d3d3d3">✔︎</td>\n\
<td align="center" bgcolor= "#d3d3d3" style="font-weight:bold">JAN</td>\n\
<td align="center" bgcolor= "#d3d3d3" style="font-weight:bold">ASIN</td>\n\
<td align="center" bgcolor= "#d3d3d3" style="font-weight:bold"><img src="fig/mono.png" width="50"></td>\n\
<td align="center" bgcolor= "#d3d3d3" style="font-weight:bold">Image</td>\n\
<td align="center" bgcolor= "#d3d3d3" style="font-weight:bold"><img src="fig/delta.png" width="150"></td>\n\
<td align="center" bgcolor= "#d3d3d3" style="font-weight:bold"><img src="fig/faber_logo.png" width="80"></td>\n\
<td align="center" bgcolor= "#d3d3d3" style="font-weight:bold"><img src="fig/amazon2.png" width="80"></td>\n\
<td align="center" bgcolor= "#d3d3d3" style="font-weight:bold">DIF</td>\n\
<td align="center" bgcolor= "#d3d3d3" style="font-weight:bold">R_DIF</td>\n\
<td align="center" bgcolor= "#d3d3d3" style="font-weight:bold">BR</td>\n\
<td align="center" bgcolor= "#d3d3d3" style="font-weight:bold"><img src="fig/faber_logo.png" width="50"></td>\n\
<td align="center" bgcolor= "#d3d3d3" style="font-weight:bold"><img src="fig/amazon.png" width="50"></td>\n\
<td align="center" bgcolor= "#d3d3d3" style="font-weight:bold">CG</td>\n\
<td align="center" bgcolor= "#d3d3d3" style="font-weight:bold">Rank</td>\n')
#<td width=80 align="center" bgcolor= "#00ff80">EVAL</td>\n<td width=80 align="center" bgcolor= "#00ff80">NEW</td>\n<td width=80 align="center" bgcolor= "#00ff80">USED</td>\n')
b.write('</tr>\n')
b.write('</thead>\n')
#b.write('</table>\n')

#b.write('<div style="height:800px; width:1755px; overflow-x:scroll; position: absolute; top: 380px; left: 40px;">\n')
#b.write('<table position="center" border="5" cellspacing="0" bgcolor="white" width=1755>\n')
#b.write('<colgroup>\n\
#<col style="width:28px">\n\
#<col style="width:156px">\n\
#<col style="width:136px">\n\
#<col style="width:95px">\n\
#<col style="width:96px">\n\
#<col style="width:280px">\n\
#<col style="width:145px">\n\
#<col style="width:145px">\n\
#<col style="width:80px">\n\
#<col style="width:80px">\n\
#<col style="width:85px">\n\
#<col style="width:100px">\n\
#<col style="width:100px">\n\
#<col style="width:100px">\n\
#<col style="width:100px">\n\
#</colgroup>\n')
# ===============================================================================================================================

# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
# 有力商品をテーブルにまとめて表示する部分
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
set_JAN = set()
counter = 0
for line in out_list:
    JAN     = line[0]
    ASIN    = line[1]
    name    = line[2]
    #rev     = line[9]
    #eva     = line[5]
    price   = line[3]
    A_price = line[4]
    dif     = line[5]
    R_dif   = line[6]
    BR      = line[7]
    url     = line[8]
    A_url   = line[9]
    group   = line[10]
    rank    = line[11]
    check = 0
    #set_JAN = set()
    if rank == 'None':
        rank = 0
    if int(rank) < 1000000 and JAN not in set_JAN:
        check = 1
    #new     = line[13]
    #used    = line[14]
    counter = counter + 1
    # ボタンをクリックすると別ウィンドウが立ち上がりモノレートの情報を表示する
    # mono_str = '<input type="button" onclick="window.open(\''+str(mono)+'\',\'_blank\')"value="MR" target="_blank" style="background-color:gold; font:11pt MS ゴシック; width:40px; height:40px" onmouseover="this.style.background=\'gray\'"onmouseout="this.style.background=\'gold\'">\n'
    #mono_str = '<input type="button" onclick="location.href=\''+str(mono)+'\'"value="Link" target="_blank" style="b    ackground-color:#ffff99" onmouseover="this.style.background=\'#99ccff\'"onmouseout="this.style.background=\'#ffff99\'">    \n'
    url_str  = '<input type="button" onclick="window.open(\''+str(url)+'\',\'_blank\')" value="R" style="background-color:gold; font:11pt MS ゴシック; width:40px; height:40px" onmouseover="this.style.background=\'gray\'"onmouseout="this.style.background=\'gold\'">\n'
    A_url_str= '<input type="button" onclick="window.open(\''+str(A_url)+'\',\'_blank\')" value="A" style="background-color:gold; font:11pt MS ゴシック; width:40px; height:40px" onmouseover="this.style.background=\'gray\'"onmouseout="this.style.background=\'gold\'">\n'
    # ===============================================================================================================================
    b.write('<tr>\n')
    if check == 1:
        b.write('<td align="center" ><p><a onClick="sound()"><input type="checkbox"></a></p></td>\n')
    #else:
        #b.write('<td align="center" bgcolor="gray"><p><a onClick="sound()"><input type="checkbox"></a></p></td>\n')
    if check == 1:
        b.write('<td align="center" >'+str(JAN)+'</td>\n')
    #else:
    #   b.write('<td align="center" bgcolor="gray">'+str(JAN)+'</td>\n')
    if check == 1:
        b.write('<td align="center" >'+str(ASIN)+'</td>\n')
    #else:
    #   b.write('<td align="center" bgcolor="gray">'+str(ASIN)+'</td>\n')
    # if check == 1:
    #     b.write('<td align="center" >'+str(mono_str)+'</td>\n')
    #else:
    #   b.write('<td align="center" bgcolor="gray">'+str(mono_str)+'</td>\n')
    if check == 1:
        #image_name = ASIN + '.jpg'
        #path = 'data/image/'+image_name
        #if os.path.isfile(path) is not True:
        #   image_name = 'No-image.jpg'
        b.write('<td align="center" height="60px"><img src=\'http://images-jp.amazon.com/images/P/'+ASIN+'.09.TZZZZZZZ.jpg\' width="60" height="50"></td>\n')

    if check == 1:
        if len(str(name))  > 100:
            name = '{:.100}'.format(name)
        b.write('<td width="300px"><a href="'+'https://delta-tracer.com/item/detail/jp/'+str(ASIN)+'" target="_blank">'+str(name)+'</a></td>\n')
        #b.write('<td>'+str(name)+'</td>\n')
    #else:
    #   b.write('<td bgcolor="gray">'+str(name)+'</td>\n')
    if check == 1:
        b.write('<td align="right"><font color="crimson" style="font-weight:bold" size="4">¥'+str(price)+'</td>\n')
    #else:
    #   b.write('<td align="right" bgcolor="gray">'+str(price)+'</td>\n')
    if check == 1:
        b.write('<td align="right"><font style="font-weight:bold" size="4">¥'+str(A_price)+'</td>\n')
    #else:
    #   b.write('<td align="right" bgcolor="gray">'+str(A_price)+'</td>\n')
    if check == 1:
        b.write('<td align="right" >'+str(dif)+'</td>\n')
    #else:
    #   b.write('<td align="right" bgcolor="gray">'+str(dif)+'</td>\n')
    if check == 1:
        b.write('<td align="right" >'+str(R_dif)+'</td>\n')
    #else:
    #   b.write('<td align="right" bgcolor="gray">'+str(R_dif)+'</td>\n')
    if check == 1:
        b.write('<td align="center" bgcolor= "#ffdead" style="font-weight:bold">'+str(int(float(BR)))+'</td>\n')

    if check == 1:
        b.write('<td align="center" >'+str(url_str)+'</td>\n')
    #else:
    #   b.write('<td align="center" bgcolor="gray">'+str(url_str)+'</td>\n')
    if check == 1:
        b.write('<td align="center" >'+str(A_url_str)+'</td>\n')
    #else:
    #   b.write('<td align="center" bgcolor="gray">'+str(A_url_str)+'</td>\n')
    if check == 1:
        b.write('<td align="center" >'+str(group)+'</td>\n')
    #else:
    #   b.write('<td align="center" bgcolor="gray">'+str(group)+'</td>\n')
    if check == 1:
        b.write('<td align="right" ><font color="crimson" style="font-weight:bold" size="4">'+str(rank)+'</td>\n')
    #else:
    #   b.write('<td align="right" bgcolor="gray">'+str(rank)+'</td>\n')
    #if check == 1:
    #   b.write('<td align="right" >'+str(rev)+'</td>\n')
    #else:
    #   b.write('<td align="right" bgcolor="gray">'+str(rev)+'</td>\n')
    #b.write('<td align="center" >'+str(eva)+'</td>\n')
    #b.write('<td align="center" >'+str(new)+'</td>\n')
    #b.write('<td align="center" >'+str(used)+'</td>\n')
    b.write('</tr>\n')
    # ===============================================================================================================================
    set_JAN.add(JAN)
    #print jan
    #print name
# ===============================================================================================================================
b.write('</div>\n')
b.write('</table>\n')
b.write('</div>\n')
#b.write('</div>\n')
#b.write('<font face="Comic Sans MS" size="5" color="white">Presented by Falcom Inc.</font>\n')
b.write('<div class="shuto"><marquee><font color="white" face="Comic Sans MS" size="4">Developed by Shuto Kawabata in 2017. All rights reserved.</marquee></div>\n')
b.write('</body>')
#b.write('</div><!--zentai-->\n')
b.write('</div><!--all-->\n')
# ===============================================================================================================================
a.close()
b.close()
