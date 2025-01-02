""" #####################################################
発想

N <= 10**6
1 <= A <= 10**9

- 基本的な調査方法
1. 1~N i まで一つずつ実行。O(N)
2. 吸収を繰り返し、OKならcount、無理ならnocount 次のiへ O(N)
..間に合わない。

2をO(1) かO(log(N))くらいにしないと間に合わない。

吸収を繰り返すプロセスについてかんがえる。
Ai = 1,1,3,4
i = 1の時
    - i=2 Ai=1 を吸収して2へ。
    - i=3 Ai=3 を吸収して5へ。
i = 2の時
    - i=1 Ai=1 を吸収して2へ。
    ...一緒

ある地点における累積値が、次の最小値より 2A 未満だった時、
それ以下に存在する全ての色は生成することができないということ。

...つまり,ある地点jにおける累積値と, Aj+1の値を比べて 2Aj+1 < jの累積 を見つけたら終了するとよさそう。

1. 昇順にソート O(NlogN)
2. 小さい順に累積和 O(N)
3. 大きい順に壁をチェックして、吸収できないor 最後まで続ける

##################################################### """
def check() :
    print(365*3)
    return


def main() :
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    cumulative_sumA = [0]
    for a in A: cumulative_sumA.append(cumulative_sumA[-1]+a)

    for i in range(N-1,0,-1) :
        if cumulative_sumA[i]*2 < A[i] : #今までの累計*2<Ai(吸収したいやつ)
            print(N-i)
            return
    else :
        print(N)
    return


if __name__ == "__main__" :
    #main()
    check()
