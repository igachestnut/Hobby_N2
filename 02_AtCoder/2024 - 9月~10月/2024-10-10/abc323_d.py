""" 
- 発想
小さい順番にスライムを合成、確定する。
resultに奇数なら追加する。

その際、Sで実行すると 1<=S<=10**9より間に合わなそう。
queueを利用して、Nの数だけ飛び飛びで実行するようにしよう。

いや、dict使えばよくね？keysで情報取得するだけ。


"""

from collections import defaultdict
def checker() :
    S = defaultdict(int)
    S[1] = 10
    S[2] = 11
    print(S)
    for i, s in S.items() :
        if s == 10 :
            S[s+10] = 5
        print(f"現在取得しているkeyは{i}です")
    print(S)
    return


import heapq

def main() :
    N = int(input())
    S = defaultdict(int)
    queue = []
    heapq.heapify(queue)

    # スライムの情報取得。サイズの位置で作業
    for i in range(N) :
        s, c = map(int, input().split())
        S[s] += c
        heapq.heappush(queue, s)
    #print(queue)
    # 結果の計算
    result = 0
    while queue :
        que = heapq.heappop(queue) #小さい順にsの取り出し
        if S[que] > 1 :
            new_s, new_c = que*2, S[que] // 2
            S[new_s] += new_c
            heapq.heappush(queue, new_s) 
            S[que] -= new_c*2 #合成後の値を少なくする。

        if S[que] == 1 :
            result += 1
            S[que] = 0

    #print(S)
    print(result)

    return


if __name__ == "__main__" :
    main()
    #checker()
