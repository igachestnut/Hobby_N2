""" 

超シンプルな仕事計算方法
result = [S[K[q]-1] for q in Q]

Sが求まってれば、O(1)で要素にアクセスできる。
ただし、K[q]-1 < 10**18 なので、メモリエラー

10**100 回実行される処理でいえること
- 一度 S(前のほう)が決まってしまえば、もう変更されることはない。

- 解く方向性
    - Queryを解いて 必要なSだけ決定作業をしていくか、
    - 最初から傾向を把握して、一つ一つの文字に対してlog(S)で導出するか。


- 傾向分析2
    - 出てくる文字の種類はせいぜい4通りだろう。
    - aB, Ab, AbaB, AbaBaBAb,
    - 0,  1,  1 0,  1 0 0 1,  1 0 0 1 0 1 1 0

    - i = 10**100 において、
        dp[i] = (dp[i-1])の逆ビットという感じ。
        
        めちゃくそ多いように見えるけど、
        bit は 2**i で増えていき、 10**18 を超えるまでは N<60でいい。
        なので処理はN = 60回実施すれば, bitの定義が完了する。

    - ではこのbitの時の数値
    - 1, 1 2, 4,,,  2**Nのようになり
    - len(S), len(S)*2**0, len(S)*2**1,,, len(S)*2**N となる。


- 傾向分析3
    - さらに言うと、aB もbit形式で整えることができる。
    - 小文字を0, 大文字を1とすると
    - 01と書くことができる。

    
- では、任意のk が与えられたとき、Sの何番目の文字なのか。を返すには...?
    - 最も簡単な返す方法 k mod len(S) ただし、10**18 mod len(S) 大きい数字ではあるので、できるだけ避けたい。
    - あらかじめmod計算させておくのは手という考えもある。

    - 出てくる全数字をdefaltdictに入れて、その数値を計算し、あとはdict[K] で出力する

    
- DPのを用いて計算すればよさそう。
    - DP[-1]の数値を流用して、あとプラスアルファの数値を作ればいいだけなんで、log(10**18)だけ調査すればよさそうである。
    


"""

def check() :
    import math
    print(math.log2(10**18))
    return

def check_s() :
    #s.isupper()
    #s.islower()
    pass

from collections import defaultdict
def main() :
    S = input()
    Q = int(input())
    K = list(map(int, input().split()))

    k_numbers = defaultdict(int)
    k_max = 0
    for k in K: 
        k_numbers[k] = ""
        k_max = max(k, k_max)
    
    # S aB を 01 とする。
    dp = [""]
    dp_1 = ""
    for i,s in enumerate(S) :
        if s.islower() : dp_1+=s.upper()
        else : dp_1 +=s.lower()
    dp.append(dp_1)

    #dpの計算 遷移1つ前のやつそのまま流用+ 1つ前のそのまま入れ変え
    for i in range(1, 60) : 
        dp_i = dp[i-1]
        for s in dp[i-1] :
            if s.islower(): dp_i+=s.upper()
            else: dp_i +=s.lower()
        dp.append(dp_i)        
    
    print(dp[:5])

    #小さい順に出てくる数字を使用して、辞書を作成する。
    now_herasu = 0
    i = 0
    for key in sorted(k_numbers.keys()) :
        while key > len(S)*2**(i) :
            i += 1
            now_herasu = len(S)*2**(i-1)
        k_numbers[key] = dp[i][key-now_herasu]
    
    result = []
    for k, q in enumerate(K) :
        result.append(k_numbers[k])

    

    
    
    

    return


if __name__ == "__main__" :
    main()
    #check()
