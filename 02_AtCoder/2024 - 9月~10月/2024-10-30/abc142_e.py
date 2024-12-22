""" #####################################################
発想

bitDPを実装しようの問題
- bitは、物事の集合を表すことができる。

N個の宝箱において、
まだ宝を開けられていない   = 0 = 0000
1番目のみ宝を開けられている = 1 = 0001
2                        = 2 = 0010
3のみ                     = 4 = 0100
つまり、開けられている状態か否かは、
2**N だけのdp配列で記入することができる。

これに対して、M 個だけのカギを使用することを考えるとき、
1~i~M のカギが存在し、
dp[i] i番目まで使用した際に考えられる全部の通り
dp[i][bit] = i番目までのカギを使用した場合で、bitのカギが開けられているとき、その位置の最小金額


- ではdpの遷移を考える
dp[i][bit] = 12
bit= 2 = 0010 の時, 12円を既に使用している。

鍵ai = 35, 開けられる宝箱数 bi = 1
C = [1] の時
key_bit = sum(2**(c-1) for c in C) = 0001
このカギを使用したときのdpというのは、
new_bit = key_bit | bit (dp[i][bit] != float("inf")-のとき)
dp[i][new_bit] = min(dp[i][new_bit], dp[i][bit]+ai)である。


- bit演算子MEMO
1. | : or演算
    ex)xx | xx 
    1101 | 1011 → 1111 が出力される。
2. & : and演算
    ex) xx & xx
    1101 & 1011 → 1001 が出力される

##################################################### """
def check() :
    a, b = 3,5
    print(a|b)
    print(bin(a), bin(b))
    print(bin(a|b))
    return


def main() :
    N, M = map(int, input().split())
    bit_dp = [[float("inf") for _ in range(2**N)]]
    bit_dp[0][0] = 0
    for i in range(M) :
        a, b = map(int, input().split())
        C = list(map(int, input().split()))
        key_bit = sum([2**(c-1) for c in C]) #keyの集合を表すbitを作成
        
        # 到達する可能性のあるbitについてdp遷移
        new_dp = [bef_dp for bef_dp in bit_dp[-1]]
        for bit in range(1 << N) :
            if bit_dp[i][bit] != float("inf") :
                new_bit = bit | key_bit
                new_dp[new_bit] = min(new_dp[new_bit], bit_dp[i][bit]+a)
        bit_dp.append(new_dp)
        #print(bit_dp)
    if bit_dp[-1][-1] == float("inf") : print(-1)
    else : print(bit_dp[-1][-1])
    return


if __name__ == "__main__" :
    main()
    #check()
