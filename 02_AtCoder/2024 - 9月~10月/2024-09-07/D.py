"""

結果 TLE

- シンプルに実行してみたけどダメだった。
    具体的なアルゴリズム、
    1. 壁の有無を格納したmapを作成。
    2. queryの実行
        1. 該当場所の調査、
        2. 上下左右に壁を探索 
        を繰り返す
    3. mapの壁総数を計算
    終了
    
- この場合の最悪計算量 O(Q * HM) > 10**9と思われる。
    HW で定義されるmapが、もしH=4 * 10**5  W=1 だった場合、
    上下の探索に最悪 HMだけかかるから。
    これをQ回繰り返すと、上記の最悪計算量になる。

"""

def cheaker() :
    return


def main() :
    H, W, Q = map(int, input().split())
    floor = [[-1 for i in range(W+2)]]
    for i in range(H) :
        floor.append([-1] + [1 for _ in range(W)] + [-1])
    floor.append([-1 for i in range(W+2)])
    #print(floor)
    #print(len(floor))
    #print(len(floor[0]))
    
    for q in range(Q) :
        R, C = map(int, input().split())
        #print(R, C)
        if floor[R][C] == 1 :
            floor[R][C] = 0
        else :
            #上調査
            u = 1
            while floor[R-u][C] == 0 : u += 1
            if floor[R-u][C] == -1 : pass
            else : floor[R-u][C] = 0
            
            #下調査
            d = 1
            while floor[R+d][C] == 0 : d += 1
            if floor[R+d][C] == -1 : pass
            else : floor[R+d][C] = 0
            
            #左調査
            l = 1
            while floor[R][C-l] == 0 : l += 1
            if floor[R][C-l] == -1 : pass
            else : floor[R][C-l] = 0
            
            #右調査
            r = 1
            while floor[R][C+r] == 0 : r += 1
            if floor[R][C+r] == -1 : pass
            else : floor[R][C+r] = 0
                
    result = 0
    for h in range(1, H+1) :
        for j in range(1, W+1) :
            result += floor[h][j]
    print(result)
    for i in range(len(floor)) :
        print(floor[i])    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
