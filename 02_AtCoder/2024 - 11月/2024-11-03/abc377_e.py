""" #####################################################
発想


同時にPを更新したときK回後のqueryはどのような配列になっているのか?
doubling (ダブリング)で解いてみようの会。

K回後の状態というのは一意に定まっている?
ので適用できそうと思ったため。

計算量(事前準備) = O(Nlog(K))
計算量(到達)? = O(lon(K))
らしい...

doublingの遷移
doubling[k+1][i] = doubling[k][doubling[k][i]]


##################################################### """
def check() :
    return


def main() :
    N, K = map(int, input().split())
    P = [-1] + list(map(int, input().split()))

    # doublingデータ構造の定義
    k_bit_len = K.bit_length()
    doubling = [[p for p in P] for k in range(k_bit_len+1)]
    for k in range(k_bit_len) :
        for i in range(1, N+1) :
            doubling[k+1][i] = doubling[k][doubling[k][i]]
    print(doubling)

    
    return


if __name__ == "__main__" :
    main()
    #check()
