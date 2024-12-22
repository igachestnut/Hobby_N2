""" #####################################################
発想

- (1,1)から右下のますに移動して、(H,W)に到着できる
- (1,1),(H,W)は必ず白
- 白= "."

- マスを良い状態にすること。
(最小回数について)

- H,W <100 より、計算量の考察。もしH,Wが、(100,100)だった場合の計算量は??
20 10 4 1
10  6 3 1 
 4  3 2 1
 1  1 1 1

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
のデータ構造???
- 二項定理


200C100?? になるのかな？
...全数調査は無理だね。
BFSの全探索は無理だね

..ではどうするか??
- 最短の塗り替え回数→どれだけ多くの白ますを踏めるのか???
- 白のオブジェクト群でNode分けし、最大に踏める数を定義するとか。
.#.#.#
#.#.#.
.#.#.# の時超めんどくさいね

####.
...#.
##.#.
####.
の時もめんどくさいね。

#####
...##
#####
#.###
#...# の時も本当にめんどくさいね


- ある地点に到達するまでに考えられる、最高白踏み回数をダイクストラ法で考えるとか？？
- 水をぶわって回して、その地点における最大を更新していく。
- すると、幅優先探索で考え方は良いことになる。1回の探索で得られる到達地点は、
常に今までの数の最大踏み回数になるので、何とかなりそう。

すると計算量は、最も大きい1回の幅優先探索は min(H,W) *2回と考えられる。
それを max(H,W)回繰り返すので、

H,W = 100,100の時、
O(H*(2H)) =O(H**2) と考えることができそう。これは十分高速

<具体的な処理方法を考える>
- 遷移イメージ
    - 現在i,jでした。sum(i,j) が0,0想定～100,100想定の計201回実施されそう。
    - 0~H+W で推移するk があるとして、任意uの時の、探索するべき(i,j)とは、
    0~u で推移するvがあるとして、
    (u-v, v)が(i,j)として探索するべき場所である。
    各場所において、右、下を検索して、その最小値(踏めなかった回数)を記載するようにする。

    
- 境界値で考える。

 

##################################################### """
from collections import defaultdict
def check() :
    """ 200C100を素因数分解したらどのようになるのか確認する

    200C100をそのまま回そうとするとやばいので、
    0~50 くらいまでの素因数と、それ以外の 
    """
    N = 30

    ue_soinnsuu = defaultdict(int)
    for i in range(N//2+1,N+1) :
        tmp_i = i
        j = 2
        while tmp_i > 1 :
            if tmp_i %j == 0:
                ue_soinnsuu[j] +=1
                tmp_i //= j
                j-=1
            j+=1
    
    sita_soinsuu = defaultdict(int)
    for i in range(1,N//2+1) :
        tmp_i = i
        j = 2
        while tmp_i > 1 :
            if tmp_i %j == 0:
                sita_soinsuu[j] +=1
                tmp_i //= j
                j-=1
            j+=1

    print(sorted(ue_soinnsuu.items()))
    print(sorted(sita_soinsuu.items()))
    combi = defaultdict(int)
    for key in ue_soinnsuu.keys():
        combi[key] = ue_soinnsuu[key]-sita_soinsuu[key]
    print("---------------------------------------------")
    print(sorted(combi.items()))
    return


def main() :
    """ ダイクストラ法っぽいけどちょっと違く、ちょっとDPっぽい解き方
    
    (i,j)の総和順に推移するuを用いて (0~u~H+W )
    i,j の総和がu だった時、次の配列を

    ※nodeは、一番下と、一番右に1マスの猶予を設ける。
    これにより、すべての(i,j)において右と下を調査することができるようになる。

    ...WAでした。
    - ひっくり返す領域は、r0,r1 c0,c1 で指定することができる。1つではない。
    つまり2 2で
    ##
    ## の時の最高率は
    ..
    .. に一気にひっくり返すことで、
    合計1回になる。

    """
    H,W = map(int, input().split())
    S = [list(input())+["."] for h in range(H)]
    S.append(["." for w in range(W+1)]) #余白を設ける
    #print(S)

    # 最短黒踏み回数を記載したnode_mapの作成
    node = [[float("inf") for j in range(W+1)] for i in range(H+1)]
    if S[0][0] == "#": node[0][0] = 1
    else :             node[0][0] = 0

    # 調査の開始
    for u in range(H+W) :
        i = min(u,H-1)
        j = max(0,u-(H-1))
        # 現在見える位置より、次の位置(右下)への最小踏み回数を計算する
        while i>-1 and j<W:
            right = 1 if S[i][j+1] =="#" else 0
            down  = 1 if S[i+1][j] =="#" else 0
            node[i][j+1] = min(node[i][j+1], node[i][j]+right)
            node[i+1][j] = min(node[i+1][j], node[i][j]+down)
            i -= 1
            j += 1
    print(node)
    print("----------------------------")
    print(node[H-1][W-1])
    return


def main2() :
    """ 
    - 境界に意識を置いて問題を解く。
    - 左上から最短を定義する方向性は変わらない。
    - 左上から見えるすべてのNode群を調査する。
    - Node軍で一番奥に到達できる。もしくはできそうなものを決定し、
    
    - 橋を作る回数を考慮するという考え方。
    - (最も遠くへ行ける白色のNode群はどこなのか?)
    """
    H,W = map(int, input().split())
    S = [["x" for w in range(W+2)]]
    for h in range(H) :
        S.append(["x"]+list(input())+["x"])
    S.append(["x" for w in range(W+2)]) #余白を設ける


    # 最短黒踏み回数を記載したnode_mapの作成
    node = [[2]+[-1 for j in range(W)]+[2] for i in range(H+2)] #[到達Node、現在の最小入れ替え回数]
    for j in range(W+2) :
        node[0][j] = 2
        node[H+1][j] = 2
    node[1][1] = 0
    def myBFS(y,x,s,node_num) :
        """ (i,j)が与えられたとき、i,jと同じ色の調査をしNode番号を記載する 

        Return
        ----------
        - query: set
            - 入り始めの境界値であるs とは異なるデータ(node_numよりも大きいnodeに該当しそうなデータ)を持つ全座標

        Note
        --------------
        - node_num: int
            - 始点
            1,1から何回入れ替え(白と黒が変わった)のか数えている番号
        - Flowについて
            - 現在時点の周囲を調べ、境界となるすべての位置をメモする。
            - メモしたものを返す。
        """
        if node[y][x] == -1:
            new_query = set()
            node[y][x] = node_num
            if S[y][x] == "x":
                return set()
            elif S[y][x] == s:
                _sides = [(-1,0),(0,-1),(1,0),(0,1)]
                for i,j in _sides:
                    new_query.update(myBFS(y+i, x+j, s, node_num))
                return new_query
            else:
                new_query.add((y,x))
                return new_query
        else :#調査したがすでに到達済みなので検証する必要なし。
            return set()     

    # 調査の開始 最終位置に到達するまで実行する
    n = 0
    query = set()
    query.add((1,1))
    while node[H-1][W-1] == -1 :
        n +=1
        print(node)
        input("enter")
        new_queue = set()
        for qy,qx in query:
            new_queue.update(myBFS(qy,qx, S[qy][qx], n))
        query = new_queue

    result = 0 if S[1][1] == "." else 1
    result += (node[H-1][W-1]+1)//2
    print(result)
    return

def main3() :
    return

if __name__ == "__main__" :
    main2()
    #check()
