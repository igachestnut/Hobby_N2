


################################################################
##Simulator

#MMDの座標を取得し、適正な誤差を与えた後シミュレーションする。
#シミュレーション内容が気に入ったら、vmdかpyautoguiで作成する。

################################################################

#グラフ作成用
import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
#ファイル操作
import os
import shutil
#gifの作成
from glob import glob
from PIL import Image
#その他情報
import datetime
import random

######################################################################
#座標計算
#入力したデータから、時間を計算して、
#

def coodinate() :
    return

######################################################################    
#以下しばらくMMD用イレギュラー
#人間っぽい動きを研究し、その法則を適用する関数の設定。


######################################################################

######################################################################

######################################################################  

######################################################################
#仮にtmpという名前の画像を作成して、
#移動するときにリネームするようにしよう。
#

#パラメータの説明
#x,y,z→座標 (ある時間での座標)
#i→時間関数　pngの枚数を決める。
#ElevationView=15 AzimuthalView=-60　→視点 



def simulator(x,y,z,i,ElevationView=15 , AzimuthalView=-60):
    #np型に変換と、zをxyの関数にする処理
    x,y,z = np.array(x),np.array(y),np.array(z)
    x_new, y_new = np.meshgrid(np.unique(x), np.unique(y))
    z_new = griddata((x, y), z, (x_new, y_new))
    
    #グラフ作成の準備
    fig , axs = plt.subplots(constrained_layout = True ,
                             subplot_kw ={'projection': '3d'})
    
    #軸と軸ラベルの設定
    axs.set_xlabel("x axis")
    axs.set_ylabel("y axis")
    axs.set_zlabel("z axis")
    #axs.set_xlim(0,1)#範囲
    #axs.set_ylim(0,1)
    axs.set_zlim(0,1)
    
    #視点
    axs.view_init(elev=ElevationView, azim=AzimuthalView)
    #elev=Elevation viewing angle 視点高さ  default=15
    #azim=Azimuthal viewing angle 方位角    default=-60
    
    #3Dの生成
    surf = axs.plot_surface(x_new,y_new,z_new)

    #画像保存
    num = i
    tmpname = "tmp{}.png".format(num)
    plt.savefig(tmpname)

    return

######################################################################
#保存したpngを使ってgifを作成する。

#gifの設定を変数で指定できる
#durationの設定　デフォルトは500[ms]
def Makegif(durationSpeed=500) :
    pictures = []
    path = "*.png"
    pnglist = glob(path)#全画像の数を調べる

    #生成した画像を取得する    
    for i in range(len(pnglist)) :
        img = Image.open(pnglist[i])
        pictures.append(img)
    
    #gifの作成→名前は仮にtmp
    pictures[0].save("tmp.gif",save_all=True,append_images=pictures[1:],
                     optimize=True,duration=durationSpeed,loop=0)
    print("gif画像は{}枚の画像から作成しました".format(len(pnglist)))

    return len(pnglist)#pngの全数

######################################################################
#フォルダ名を指定して、saveする関数
#作成したファイルをリネームもする。

#Newname→画像の名前。dirなら「名前」のフォルダ。pngなら「名前_1.png」が作成
#ちなみに画像の名前は「.png」など入れなくても問題ないように設計

#入力　→　作成したpngの枚数,新しい名前
def Movefile_rename(Sheet,Name="tmp") :
    dirname = "simulation(png,gif)"
    Date = str(datetime.date.today())

    #画像・gif名重複チェック
    Name = duplicateCheak(Name,dirname,Date)
    
    #保存するディレクトリの生成
    os.makedirs("{}/{}/{}_png".format(dirname,Date,Name), exist_ok = True)
    
    #gifの移動
    #同じフォルダ内にあるtmp.gifというgifを
    #./simulation/日付/tmp.gifという風に保存する
    shutil.move("tmp.gif","./{}/{}/{}.gif".format(dirname,Date,Name))

    #pngの移動
    #同じフォルダ内にあるtmp1.pngという画像を
    #./simulation/日付/tmp/tmp_1.pngという風に保存する
    for i in range(Sheet) :
        shutil.move("tmp{}.png".format(i),
                    "./{}/{}/{}_png/{}_{}.png".format(dirname,Date,Name,Name,i))
    return

#ファイル名重複チェック
def duplicateCheak(name,dirname,Date) :
    def Namecheak(name) :
        for i in range(len(Existing_gifList)) :
            if name in Existing_gifList[i] :
                print("File duplication Error")
                print("移動先フォルダに同名のファイルが存在します。")
                print("新しいgif又はpng名を設定してください")
                print("もし上書きしたい場合は空白のまま「Enter」を押してください")
                print("重複元ファイル名{}".format(name))
                print("")
                Newname = input("新しい画像・gif名:")
                if Newname == False :
                    return name,True#空白→処理終了（上書き）
                else :
                    return Newname,False#もう一度やり直し
        return name,True#何も重複が見つからなかったとき→処理終了

    #SubMain-Start####################################################
    #移動先ディレクトリのpathの取得とリストの生成。
    existing_path = "./{}/{}/*.gif".format(dirname,Date)
    Existing_gifList = glob(existing_path)

    #重複チェック開始
    Result = False
    while Result == False :
        name ,Result = Namecheak(name) #Result = Trueになるまで繰り返す
        continue
    
    return name

######################################################################
######################################################################
#Input()
#情報

#座標
n = 10
x = list(range(n))
for i in range(n,0,-1) :
    x.append(i)
for i in range(n) :
    x.append(i)
y = list(range(3*n))


#時間ウエイト


######################################################################
##Main

name = "Simulation1"
Sheet = min(len(x),len(y))

#画像作成と、pngの仮名前の出力
for i in range(len(x)) :
    z = [random.random() for _ in range(3*n) ]
    simulator(x,y,z,i)


#gif画像の作成
Makegif(durationSpeed=100)

#画像の移動とリネーム
Movefile_rename(Sheet,name)






