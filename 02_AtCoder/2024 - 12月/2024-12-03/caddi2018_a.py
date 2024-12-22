""" #####################################################
発想

最大公約数として考えられるもののうち、最も大きいもの？
N個に因数分解
全てをかけあわせるとPになる

N個の数字において、
最大公約数(全て%ans==0)になるansを求める。
この場合いえること 

N個だった場合、
P%(ans**N)==0 であることがわかればよい。

- 計算量
    - ans**N<=P の時実行すればよい
    - N>1 の時、O(sqrt(P)(のN-1乗根))となる。
    - N==1 なら、ans=P O(1)でよい

    
計算量を向上させる工夫
1. 一度2で割り切れることが分かった場合、
公約数には2の倍率が含まれる。
→Pを2で割りつつ、resultを2かけるとさらに効率になりそう

....
もしかして、素数**i ~= 10**12程度で、Pも同程度だから、
計算しにくいって話?
かなり可能性があるね。
while文によって、必ずiの倍数で割り切れないか調査しているので、
iで割り切れるとき、i-1以下では必ず割り切ることができない。
→iをいちいち1に戻さなくてもよさそう。

あと、sqrt(P)でいい？？？？



....方向性を大きく変えるなら、
最初にPを素因数分解する。
この際の割れた数と種類をdefaltdictに入れとく。
そのあと、各配列にN以上かどうか検査してって、N以下になるまで各vvalueを減らしつつ、resultに蒸散する。


##################################################### """
def check() :
    return


def main() :
    """ TLEでした。もしかしたらP%(i**N)が大きすぎるための可能性

    一応pypyでも出してみる 
    →MLE とREでした。
    メモリ不足ですね。

    もう一工夫が必要
    """
    N,P = map(int, input().split())
    if N==1 :
        print(P)
        return
    result = 1
    i=2
    while P>=i**N :
        if P%(i**N) ==0 :
            result = i
        i+=1
    print(result)
    return

def main2() :
    N,P = map(int, input().split())
    if N==1 :
        print(P)
        return
    result = 1
    i=2
    while P>=i**N :
        if P%(i**N) ==0 :
            result *=i
            P = P//(i**N)
            i = i-1
        i+=1
    print(result)
    return

import math
from collections import defaultdict
def main3() :
    """ 素因数分解して答えを導出する方法 """
    N, P = map(int, input().split())
    if N ==1:
        print(P)
        return
    
    P_lim = math.sqrt(P)
    factors = defaultdict(int)
    a = 2
    while a < P_lim :
        if P%a ==0:
            factors[a] +=1
            P = P//a
            a -= 1
            if P<a:
                break
        a +=1
    
    #print(factors)
    result = 1
    for key,value in factors.items() :
        while value >= N :
            result *= key
            value -= N
    print(result)
    return

if __name__ == "__main__" :
    main3()
    #check()
