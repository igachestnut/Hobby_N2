""" #####################################################
発想

https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_t
- 2つの文字列における、共通部分列で、最長のものを求める問題

- S,Tの2次元dpを考える?
- 1~i~S 実行する
    - i において、最も右に位置する

- dp[i][j]: 0~i, 0~j までにおける、最長部分文字列の長さ。
- dpの遷移
    i の時 0~j~T には、それまでにおける最長部分列の長さが記載される。
    なので、作るとき、dp[i][j-1] + s==t? かどうかの調査をする
    i+1 の時 上の情報を引き継ぐ。sp[i-1][j] と新規に作成する理論値の比較を行う。
##################################################### """
def check() :
    return


def main() :
    """ tokyo,kyotoがダメ
    [[0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 1, 1], 
    [0, 0, 0, 1, 1, 2], 
    [0, 1, 1, 1, 1, 2], 
    [0, 1, 2, 2, 2, 2], 
    [0, 1, 2, 3, 3, 4]]
    - 2回o が出てきてしまうんご
    """
    S = input()
    T = input()
    dp = [[0 for j in range(len(T)+1)] for i in range(len(S)+1)]
    for i,s in enumerate(S) :
        for j,t in enumerate(T) :
            dp[i+1][j+1] = max(dp[i+1][j]+ int(s==t), dp[i][j+1])
    print(dp[len(S)][len(T)])
    print(dp)
    return


def main2() :
    S = input()
    T = input()
    dp = [[0 for j in range(len(T)+1)] for i in range(len(S)+1)]
    for i,s in enumerate(S) :
        for j,t in enumerate(T) :
            dp[i+1][j+1] = max(dp[i][j]+ int(s==t), dp[i+1][j], dp[i][j+1])
    print(dp[len(S)][len(T)])
    #print(dp)
    return



if __name__ == "__main__" :
    main2()
    #check()
