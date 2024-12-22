""" #####################################################
発想

2024/06/23 竹田海渡が答えを見る前に作成

横法に移動した回数 shortcat
移動距離x,y u,w
u+w - shortcat
で算出できそう

//////////////////////////////////////////////////////////////
- shortcatの計算方法
case dis=1
[., s][e, .] = 0
  ][s, e][   = 1

case dis=2
[., s][., e] = 1
  ][s, .][e, = 1
  
case dis=3
 s][., .][e, = 1
[s, .][., e] = 2

--------------
MEMO 1
0 = dis // 2 = 1 // 2
1 = dis // 2 = 2 // 2
1 = dis // 2 = 3 // 2
short_catの最低保証 = abs(Sx - Tx) //2 である。

--------------
MEMO 2
case1とcase3 の(abs(Sx-Tx)%2==1)において、+αのショートカットが起こるには
以下のどれかを満たす
1. dis_y > 0であること。(必ず横方向における最短ルートを通ることができること)
2. 左に位置する点において、タイルの左にある⋀終了地点においてタイルの右にある 
    - (Sx < Tx and (Sx+Sy) %2 == 0) 左に位置する点ががSx  
    - (Tx < Sx and (Tx+Ty) %2 == 0) 左に位置する点がTx
    のいずれかを満たすこと

--------------    
MEMO 3
case2 において、+αのショートカットが起こるには、
以下を満たす
1. dis_y >= 1であること。(右が壁でも、上に移動すると右にshortできる)

---------------
MEMO 4
竹田海渡はさらに見落としていた。
縦移動できる回数だけ、どんな状況でもshortカットが可能であると
(右が壁でも、上に移動すると右にshortできる)
つまり、
short_cat = min(dis_x, dis_y) が最低保証である。

これに加えて、横方向に移動しなければならない際、必要なshortcatがMEMO2,MEMO3で定まりそう
if dis_x > dis_yの場合、
    dx = dis_x - dis_y #dx=残り横方向に移動しなければならない距離


##################################################### """
def main() :
    Sx, Sy = map(int, input().split())
    Tx, Ty = map(int, input().split())
    dis_x, dis_y = abs(Sx-Tx), abs(Sy-Ty)

    #short catの計算 1.斜め移動
    short_cat = min(dis_y, dis_x)
    #print(f"shrot_cat1:{short_cat}")
    
    #short catの計算 2.残りの横方向の距離
    if dis_x > dis_y :
        dx = dis_x - dis_y
        
        short_cat += dx // 2 #short_catの計算 (基本的な横方向移動における最低保証)  
        #print(f"shrot_cat2:{short_cat}")  
        if (dx % 2 == 1) and ((Sx<Tx and (Sx+Sy) %2 == 0) or (Tx<Sx and (Tx+Ty) %2 == 0)) :
            short_cat += 1
        #print(f"shrot_cat3:{short_cat}")
    
    #print(f"xdis{dis_x}, ydis{dis_y}")
    #print(f"shrot_cat3:{short_cat}")
    
    print(dis_x + dis_y - short_cat) 
    return


if __name__ == "__main__" :
    main()
    
def main2() :
    """ めっちゃ短くコード書いてみたら """
    Sx, Sy = map(int, input().split())
    Tx, Ty = map(int, input().split())
    dis_x, dis_y = abs(Sx-Tx), abs(Sy-Ty)

    #short catの計算 1.斜め移動
    short_cat = min(dis_y, dis_x)
    
    #short catの計算 2.残りの横方向の距離
    if dis_x > dis_y :
        dx = dis_x - dis_y    
        short_cat += dx // 2 #short_catの計算 (基本的な横方向移動における最低保証)  
        if (dx % 2 == 1) and ((Sx<Tx and (Sx+Sy) %2 == 0) or (Tx<Sx and (Tx+Ty) %2 == 0)) : #距離奇数における、左開始、右終わりかどうか
            short_cat += 1
    
    print(dis_x + dis_y - short_cat) 
    return
