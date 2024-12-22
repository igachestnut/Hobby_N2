""" 連続する部分列のうち和がSとなるものが存在するか判断する

存在する= YES

- 存在する場合を列挙する
- 0~N 以内のi<=j となるi,j があり、sum(A[i:j+1])がSならTrue
- さらに0~N*2 なる k,l があり、sum(A[k:l+1])がSならTrue

- ∞ ということで、Sがsum(A)よりも大きかった場合
sum(A)1回につき、配列A分は繰り返される→最初からmod演算してOK



....Aが2回繰り返される配列B のうち、連続する可能性のある数値の合計
を出すには、
累積和を使用して。

Bのうち、現在iから始めるなら、i+1~i+N までの格納している配列に着目する,1~Nの分布を持つ変数をjとすると
- B[j+i]-B[i] == S: 
    print(Yes
- B[j+i]-B[i] > S :
    bisect の下
- B[j+i]-B[i] < S:
    bisect の上

逆にbisectで調査するS は、駆らなずB[i]分を含むので、B[i]+Sにすると調査できそう
"""
def check() :
    return

import bisect
def main() :
    N,S = map(int, input().split())
    A = list(map(int, input().split()))
    modS = S % sum(A)
    B = [0]
    for i in range(N): B.append(B[-1]+A[i])
    for i in range(N): B.append(B[-1]+A[i])

    #print(B)
    result = "No"
    for i in range(N) :
        x = bisect.bisect_left(B, B[i]+modS)
        #print(modS+B[i], x, B[x], B[i])
        if B[x]-B[i] == modS :
            result = "Yes"
            break
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
