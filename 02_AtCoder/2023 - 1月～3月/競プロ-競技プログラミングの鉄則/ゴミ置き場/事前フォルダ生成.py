import datetime
import os

###############################################################
#注意
#このアルゴリズムはファイル番号が間違って出力されてしまうため
#実行しないこと。（データが壊れています）

###############################################################
#作りたいファイル名生成
"""
pyName = "Prog"
syouName = ["1-アルゴリズムと計算量","2-累積和","3-二分探索",
            "4-動的計画法","5-数学的問題","6-考察テクニック",
            "7-ヒューリスティクス","8-データ構造とクエリ処理",
            "9-グラフアルゴリズム","10-相合問題"]

Newfilename = []

a = [0,6,11,16,26,36,46,51,61,71]    

j = 0
for i in range(77) :
    Newfilename.append(os.path.join(syouName[j] , "{}_A{}.py".format(pyName,i+1)))
    if i < 72 :
        if i == a[j+1] :
            j += 1

#フォルダ作成
for i in range(len(syouName)) :
    Newdirname = os.path.join("./",syouName[i])
    os.makedirs(Newdirname,exist_ok=True)

#ファイル作成(python)
for i in Newfilename :
    with open(i , mode="w",encoding = "UTF-8") as f :
        if not os.path.isdir(i) :
            f.write("")

"""
