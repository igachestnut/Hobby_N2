def cheaker() :
    return


def main() :
    N = int(input())
    
    carpet = create_carpet(N)
    
    #出力
    for y in range(3**N) :
        print("".join(carpet[y]))
    
    return

def create_carpet(N:int) :
    """ 入力されたレベルを用いて、カーペットを作成する関数 """
    
    #全て黒(#)の配列作成
    carpet = [['#' for i in range(3**N)] for j in range(3**N) ]
    
    #レベルに応じて順次白(.)の入力
    for level in range(N+1) :
        if level == 0 :
            continue
        #任意levelによる中心の色塗り作業 #分割した識別座標で色を塗る
        for y in range(0, 3**N, 3**level) :
            for x in range(0, 3**N, 3**level) :
                #色塗り作業
                drow_range = int(3**(level-1))
                for yw in range(drow_range) :
                    for xw in range(drow_range) :
                        #print(f"y{y+drow_range+yw}, x{x+drow_range+xw}")
                        carpet[y+drow_range+yw][x+drow_range+xw] = "."
                        #print("処理がされました")
    return carpet
    
                
                
                


if __name__ == "__main__" :
    main()
    #cheaker()
