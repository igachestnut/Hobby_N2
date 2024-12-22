"""
def cheak(x,y) :
    if y :
        print(x)
        return
    else :
        print("empty")
        return

x,y = 3,""
cheak(x,y)
cheak(x)
"""
#検証したかった内容
#defでyその者が無かった時、emptyになるかErrorになるか
#結果→Error
#内容がなくても入れなければならないようだ。

"""
def cheak2(x,y=5) :
    if y :
        print(x)
        return
    else :
        print(y)
        return

x,y = 3,""
cheak2(x,y)
cheak2(x)
"""
#検証したかった内容
#予め変数にデフォルトの表示を入れていれば


def cheak3(x,num_y=3,num_z=5) :
    if z == 6 :
        print(z)
        return
    else :
        return

x,y,z = [],[],6
cheak3(x,num_z=z)

#変数内のdefultは指定できるのか。

    

