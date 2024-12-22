""" #####################################################
発想

Q の材料をうまいこと振り分けて、
A,Bの料理を最大個数作りたいのコーナー

Q <= 10**6 であり、
A, B 2つの種類をふるまう
→出力される最大の答えは 2*10**6 だけ。この構成?を調べる?
Aがx個, Bがy個作成されたとき、可能か否か?という感じ?
いや、AとBの組み合わせでの出力なので、10**6 **2だね。

dpが適用できそうではあるが...
dp[i] iは、料理の提供数。
i 個だけの料理が提供されたとき、各状態の最良個数 項目がなぁ多いな
Q_max 個最大
ABの構成 [0, 0], [1, 0], [0, 1], [2, 0], [1, 1], [0, 2]...


..逆にAのMAXまで調べる、
そこからA=0になるまで実施。
Bを追加できるだけ追加し、そのうちの最大を検証するというもの。
a を固定してbを考えた結果のプログラム。

////////////////////////////////////////////////
ちなみに解説でも同じ考え方だった。
ただ、aを0~max(Q)まで実施し、その時のmin(b_count)(Bを追加できるだけの数計算)
して計算していた。(加算形式ではなくすべて余りなし除算)だった。
##################################################### """
def check() :
    return


def main() :
    N = int(input())
    Q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # Aの最大を定義、そこから引いていく
    a_count = float("inf") #A,Bの最大数
    for i in range(N) :
        a_count = min(a_count, Q[i]//A[i] if A[i]>0 else float("inf"))
    
    result = a_count
    tmp_Q = [q-a*result for q,a in zip(Q, A)] #残りの空き容量
    b_count = 0
    # Aを順次引いていき、追加できるだけのBを定義していく
    for a in range(a_count, -1, -1) :
        while all(tq >= 0 for tq in tmp_Q) :
            b_count += 1
            for n in range(N) : tmp_Q[n] -= B[n] 
        result = max(result, a+(b_count-1))
        for n in range(N) : tmp_Q[n] += A[n] #a_count を一つ引き、余った材料を追加する

    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
