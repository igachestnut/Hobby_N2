"""
100*100の計算量
全探索
    
"""


def cheaker() :
    return


def main() :
    H, W = map(int, input().split())
    Land = []
    for _ in range(H) :
        Land.append(input())
    
    count = 0
    for i in range(1,H-1) :
        for j in range(1, W-1) :
            #print(i,j)
            small_land = [Land[i-1][j-1:j+2], Land[i][j-1:j+2], Land[i+1][j-1:j+2]]
            if is_donatu(small_land) :
                count += 1
    print(count)
    return

def is_donatu(small_land) :
    """ 入力された文字列がドーナツかどうか返す関数 """
    #print(small_land)
    if small_land[0] == '###' and small_land[1] == '#.#' and small_land[2] == '###' :
        return True
    else :
        return False
    


if __name__ == "__main__" :
    main()
    #cheaker()
