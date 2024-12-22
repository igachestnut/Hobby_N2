""" #####################################################
発想

- 上下左右の2マスが黒色で塗られている部分は描画可能。
- 孤立している#があるならFalse それいがいならTrue
##################################################### """
def check() :
    return


def main() :
    H, W = map(int, input().split())
    campas = [[0 for j in range(W+2)]for i in range(H+2)]
    for i in range(H) :
        S = list(input())
        for j,s in enumerate(S) :
            if s == "#" :
                campas[i+1][j+1] = 1
    
    # 隣接マスの調査 O(H*W*5)
    find_masu = [(-1,0), (0,-1), (0,0), (1,0), (0,1)]
    for i in range(1, H+1) :
        for j in range(1, W+1) :
            if campas[i][j] == 0: continue
            black = 0
            for (x,y) in find_masu :
                black += campas[i+x][j+y]
            if black == 1 :
                #print(i, j)
                print("No")
                return
    print("Yes") 
    return


if __name__ == "__main__" :
    main()
    #check()
