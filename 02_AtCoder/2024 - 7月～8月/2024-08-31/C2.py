""" 
実装の高速化を目指す。

1. 等差数列の和をO(1)で実装 
2. l=rの際は等差数列を満たす→result += Nを用いる
"""

def cheaker() :
    return

def main() :
    N = int(input())
    A = list(map(int, input().split()))
    result = 0
    r = 0 #右の位置
    
    #尺取り法を用いて該当する等差数列を特定する。(l < rの時の計算)
    for l in range(N) :
        if l < r : #終了位置に到達していない場合pass
            continue
        
        #等差数列の差を調査（同じ要素はpassする）
        if r == N-1: break
        
        #等差数列の差を調査
        r = l + 1 #始点の位置調整
        d = A[r] - A[l]
        
        #次の要素の有無を確認しつつ、終了位置まで調査
        while r != N-1 and A[r+1] - A[r] == d :
            r += 1
        result += v2_nutural_arithmetic_sequence(r-l)
        
    print(result+N) #l=rの値を加算した答えを出力する。
    return

def nutural_arithmetic_sequence(x) :
    """ 初項1, 等差1, 終わりxの数列の和を算出する関数 """
    return sum(range(1, x+1))

def v2_nutural_arithmetic_sequence(x) :
    """ 初項1, 等差1, 終わりxの数列の和を計算する """
    return int(x*(x+1)/2)



if __name__ == "__main__" :
    main()
    #cheaker()
