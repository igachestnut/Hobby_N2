#ライブラリのインポート
from PIL import Image
import os

#画像を入れる箱を準備
pictures=[]

name = os.listdir()
print(name)
#pngだけのリストを作成するため、
#逆順からリストを査定する
for i in range(len(name)-1,-1,-1) :
    if ".png" in name[i] :
        print("a")
        pass
    else :
        a = name.pop(i)

print(name)

#画像を箱に入れていく
"""
for i in range(4):
    pic_name='mikan' +str(i+1)+ '.jpg'
    img = Image.open(pic_name)
    pictures.append(img)

#gifアニメを出力する
pictures[0].save('anime.gif',save_all=True, append_images=pictures[1:],
optimize=True, duration=500, loop=0)
"""

"""
もし、あるパスのみのデータを抽出したいとき
import glob
 
path = './dir/*.txt'
 
list1 = glob.glob(path);
 
print(list1)
"""


"""
もしファイルのみ抽出したい場合
import os
 
path = './dir'
 
filelist = []
 
for f in os.listdir(path):
  if os.path.isfile(os.path.join(path, f)):
    filelist.append(f)
 
print(filelist)
"""


"""
#もしディレクトリのみ抽出したい場合
import os
 
path = './dir'
 
filelist = []
 
for f in os.listdir(path):
  if os.path.isdir(os.path.join(path, f)):
    filelist.append(f)
 
print(filelist)
"""
