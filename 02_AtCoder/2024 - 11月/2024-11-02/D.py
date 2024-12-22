""" #############################################

ますの移動できるものは全部でどんな通りがある?を調査したいコーナー

H*W <100
全数調査をできる。

ただ、
1回の調査において、10000回程度に抑える必要がある。
もし10*10のマスですべてが空マスであるとき、

左上からの移動できるますのバリエーションを調査するとき
2通り、2通り、2通り
2通り、3通り、3通り
2通り、...
...
1通り、2通り、2通り

のようになる。
各マスにおける、移動のバリエーションは2*...とおり？

これは概算だが、
K=11 の時、最大の移動方法は2**K ~ 3**K くらいありそう。

できるだけ上優先、左優先の順番の深さ優先探索を行うと、数は出そう。
(各Nodeにおいて、移動できる位置を保持できる。どんなに入り組んだ調査をしても、直前まで全数調査しているためかぶりが生じることはない)

K<= 11より、各Nodeにおいて、
移動できる数というのを 最大4だけ調査することになる。
K!だけの処理量
4K!になりそう。= 10**9 である。アウト。
これをどうにかして10**5程度まで抑えることができるのだろうか...

...答え合わせ
4K!と思っていたが違うらしい、
選び方が4通りあるのをK回繰り返すので、
3**K でよかった。
=177147 回
厳密には初期状態では上下左右に移動できる。4通り
移動し始めたら、来た道に戻ることはできないので3通り、以降同じ
計算量は HW * 4*3**(K-1) となり 10**8で何とかなりそう。ということ



痛い間違いをしたね。
選び方がすべてのNodeに転移が可能な時だけ順列の計算量になるんだと,,,いうことですね

- ではBFSを実行してみよう。
行けるマスといけないマスの状態を渡すためにはどうしたらよいのだろうか。


############################################# """
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def check() :
    #print(factorial(11))
    print(pow(3,11))
    return



import sys
sys.setrecursionlimit(10**8)
def main() :
    H, W, K = map(int, input().split())

    # mapの作成
    block_map = [[False for j in range(W+2)] for i in range(H+2)]
    for i in range(H) :
        S = list(input())
        for j, s in enumerate(S) :
            if s == "." :
                block_map[i+1][j+1] = True #空きマスを記載する

    def BFS(i:int, j:int, k:int, ans:int) :
        """ マス目を調査する関数 
        
        parameters
        -----------
        - i,j:int,int
            現在のマス。1~i~H, 1~j~W で定義する。

        - k : int
            現在のマスの深さ
        - ans : int
            最終位置に到達できた回数を記載する。
        
            
        MEMO
        ----------
        - 条件1 : 潜ればよい量をKとして定義しておくこと
        - 条件2 : 現在行くことができるmap状況を定義しておくこと。
            グローバルなマップに記載するようにしたいが...
        
        """
        # 終了条件 もう潜る必要がない場合にans+1する
        if k == K :
            return ans+1
        
        # 行きがけの処理 - 現時点から上下左右を調査し、答えを取得する
        block_map[i][j] = False 
        if block_map[i-1][j] == True : ans = BFS(i-1, j, k+1, ans)
        if block_map[i+1][j] == True : ans = BFS(i+1, j, k+1, ans)
        if block_map[i][j-1] == True : ans = BFS(i, j-1, k+1, ans)
        if block_map[i][j+1] == True : ans = BFS(i, j+1, k+1, ans)

        # 帰りがけの処理。現在の場所を踏む必要がなくなったため元に戻す。
        block_map[i][j] = True
        return ans
    
    # 全数調査の開始
    ans = 0
    for h in range(1, H+1) :
        for w in range(1, W+1) :
            if block_map[h][w] == True :
                ans += BFS(h, w, 0, 0)
    print(ans)
    return


if __name__ == "__main__" :
    main()
    #check()
