""" #####################################################
発想

繰り返し回数の計算orderを考えてみる。

N を２つに分け続ける。
すべての要素が1, 0になるまで実行する。

N < 10**17
10**17 を2で割り続けた結果、の回数
= 60回かな

片方を計算するだけなら 60回必要である。
ただ、すべてを計算しようとすると、
60 + 59*2 + 58*4... 1*2**60 となる。
これは計算間に合わない。

- MEMO
あるxがあるとき、それの答え = x//2, x//2 + x%2である。
下から順に X(list) を計算していけば???
答えにたどり着きそう。
すべて素数でも、xの種類は、logN だけしか生じないはず。(エスパーポイント)

##################################################### """
from collections import defaultdict

def check() :
    return


def main() :
    N = int(input())
    
    # 1.Xの除算過程に出てくるすべてのxを列挙
    X = defaultdict(int, {N: -1}) # Nを割ったときに生じる数字列
    queue = set()
    queue.add(N)
    while queue :
        new_queue = set()
        for que in queue :
            x1, x2 = que//2, que//2+que%2
            if x1 > 1 : new_queue.add(x1)
            if x2 > 1 : new_queue.add(x2)
        for nq in new_queue : X[nq] = -1
        queue = new_queue

    X[1] = 0
    for key in sorted(X) : #小さい順にソートして取り出し
        #print(key)
        if key == 1 : continue
        else :
            #print(X[key//2], X[key//2 + key%2])
            X[key] = key + X[key//2] + X[key//2 + key%2]
        #print(X)
    print(X[N])
    return


if __name__ == "__main__" :
    main()
    #check()
