""" 任意マスに加湿器が置かれているとき、
何マスが加湿されていそう???


- BFS? ダイクストラ法で調べる???
- 全Hのqueryを作ります。
- queryがなくなるまで実行します
- 全てのqueの上下左右に到達し、その時点のMaxを残り加湿領域を記入する
- もし新しい床ますならOK, それ以外ならFalse
- 計算量
    - 全マスにおける最初のqueryを見つける = O(HW)
    - 全queryを全マスに到達 or queryがなくなるまで実行する。O(HW)
        (前の処理の積ではなく、和になる。結局ＤがH*W でも、一度到達した地点からは再度調査はしないため)


"""

def check() :
    return


def main() :
    H, W, D = map(int, input().split())
    S = ["#"*(W+2)]
    for h in range(H) :
        S.append("#"+input()+"#")
    S.append("#"*(W+2))    
    wet_dis = [[0 for w in range(W+2)]for h in range(H+2)]    

    # 調査開始位置の取得
    query = []
    for i in range(1, H+1) :
        for j in range(1, W+1) :
            if S[i][j] == "H" :
                query.append([i,j])
                wet_dis[i][j] = D+1
    
    # 調査の開始
    while query :
        new_query = []
        for [qi,qj] in query :
            if wet_dis[qi][qj] == 1 :#これ以上調査不可能
                continue
            next_wd = wet_dis[qi][qj]-1
            _side = [(-1,0), (0,-1), (1,0), (0,1)]
            for si,sj in _side :
                if S[qi+si][qj+sj] == "#" :
                    continue
                elif wet_dis[qi+si][qj+sj] > 0:
                    continue
                else :#"."かつ、未到達領域
                    wet_dis[qi+si][qj+sj] = next_wd
                    new_query.append([qi+si,qj+sj])
        query = new_query
    
    result = 0
    for hw in wet_dis:
        for w in hw:
            if w >0:
                result += 1
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
