""" #####################################################
発想

- 全ての商品を買いますが、割引券を用いて購入総額を最小にしたい！
- A= [4,4,2,2,1,1]
- M = 2 だった場合。
- i=1,2 の時に割引券を一枚ずつ使用すると、総額が最小になりそう。
- これは、割引券を1枚使用したときの数値が、最も小さくなってくれるならということ。
- すると、heapqを使って、常に最大の値段のものを取り出して半分にしたのち、元の戻す感じにすると、
heapqの処理で、必ず最大をとりだっせる


- [解説](https://img.atcoder.jp/abc141/editorial.pdf?_gl=1*jaruer*_ga*MTUxNDMzNzU4MC4xNzI3NjI0OTk3*_ga_RC512FD18N*MTczMzQ0NTMzMC4xNTMuMS4xNzMzNDQ2MTYzLjAuMC4w)
- 上記のアルゴリズム(商品を順番に購入して、割引券を品物ごとにまとめて使う代わりに、割引券を一つ使うたびに、ひとつの品物を選んで半額にするとしてもかまわないこと)について数学的に証明しようとすると

##################################################### """
def check() :
    return


import heapq
def main() :
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [-a for a in A]
    heapq.heapify(B)
    while M>0:
        b = -heapq.heappop(B)
        b = b//2
        M-=1
        heapq.heappush(B,-b)
    result = 0
    for b in B:
        result += -b
        #print(b)
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
