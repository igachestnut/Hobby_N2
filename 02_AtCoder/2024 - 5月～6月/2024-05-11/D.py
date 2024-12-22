""" #######################################

結果
- wa + TLE

    N^2処理をしてしまった。(for文の中にsum)
    
    不明な計算間違い。

########################################## """

def cheaker() :
    return


def main() :
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A_len_str = [10**len(str(a)) for a in A]
    
    # ある数bairituの倍率を計算する
    bairitu = [1 for _ in range(N)]
    for n in range(N-1) :
        bairitu[n] = n + sum(A_len_str[(n+1):])
    # sumの最悪計算量はNなので、N^2となってしまいそう。
    
    #最後数の係数を計算
    bairitu[-1] = N-1
    
    result = 0
    for i, a in enumerate(A) :
        result += a * bairitu[i]
        result %= 998244353
    
    print(result)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
