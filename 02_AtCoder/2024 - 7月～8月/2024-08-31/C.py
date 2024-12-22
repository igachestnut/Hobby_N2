def cheaker() :
    a = nutural_arithmetic_sequence(3)
    print(a)
    return


def main() :
    N = int(input())
    A = list(map(int, input().split()))
    result = 0
    r = 0 #そのindexにおいて、計算を必要とするならFalse。passするならTrue　→タイプミス。右の位置
    
    #尺取り法を用いて該当する等差数列を特定する。
    for l in range(N) :
        if l < r : #終了位置に到達していない場合pass
            continue
        
        #等差数列の差を調査（同じ要素はpassする）
        if r == N-1:#リストの最後の要素に到達
            result += 1
            break
        else :
            r += 1
            
        #等差数列の差を調査
        d = A[r] - A[l]
        
        #次の要素の有無を確認しつつ、終了位置まで調査
        while r != N-1 and A[r+1] - A[r] == d :
            r += 1
        #print(f"r{r}, l{l}")
        result += nutural_arithmetic_sequence(r - l+ 1) -1
        
    print(result)
    return

def nutural_arithmetic_sequence(x) :
    """ 初項1, 等差1, 終わりxの数列の和を算出する関数 """
    return sum(range(1, x+1))


if __name__ == "__main__" :
    main()
    #cheaker()
