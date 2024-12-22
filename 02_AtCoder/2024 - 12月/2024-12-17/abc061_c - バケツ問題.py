""" #####################################################
発想

- 空の配列がある
- この配列に整数を挿入する。
- 終わった後、K番目に小さい数を求める
- 


解説...
バケツ問題をとく 
    
    - 長さ10**5の配列numを用意する
    - 全ての値は0で初期化する
    - ループを使ってnum[ai]をbiに加算する
    - 小さい順に見て、Kを超えるまで調査する。

    ...やり方別に知ってたね
##################################################### """
def check() :
    return

from collections import defaultdict
def main() :
    N,K = map(int, input().split())

    numbers = defaultdict(int)
    for i in range(N) :
        a, b = map(int, input().split())
        numbers[a] += b
    
    before_a = 0
    x = 0
    for key in sorted(numbers.keys()) :
        if x>=K :
            print(before_a)
            return
        x += numbers[key]
        before_a = key
    print(key)
    return


if __name__ == "__main__" :
    main()
    #check()
