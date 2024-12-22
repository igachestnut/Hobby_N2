def cheaker() :
    return


def main() :
    Sx, Sy = map(int, input().split())
    Tx, Ty = map(int, input().split())
    
    #各方向に直線移動した時に想定されるタイルをまたいだ回数 u=x方向, w=y方向
    u, w = 0, 0
    
    #縦方向の移動出力
    w = abs(Sy - Ty)
    
    #横方向の移動出力
    dis_x = abs(Sx - Tx)
    extra_u = 0
    if dis_x % 2 == 1 :#距離が奇数の場合 特殊ケースの計算
        #x方向において、小さいほうから大きいほうへ右に移動する場合を考える
        if Sx < Tx :
            if (Sx + Sy) % 2 == 1 and w <= 0:#小さいほうの始点が右タイル
                print("ddd")
                extra_u = 1
        elif Tx < Sx :
            if (Tx + Ty) % 2 == 1 and w <= 0:#小さいほうの始点が右タイル
                extra_u = 1
        else :
            print("入力がおかしいです")
    u = abs(Sx - Tx)//2 
    print(f"w{w}: u{u}")
    
    #距離の出力 縦方向の距離+横方向の移動(縦移動の必要回数だけ斜めに移動)
    print(w + max(0, u-w)+extra_u)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
