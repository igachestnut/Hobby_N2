""" #####################################################
[解説](https://img.atcoder.jp/agc013/editorial.pdf)
...よくわからん。
でも、愚直に計算した結果、傾向がわかり、その傾向を用いて答えを出す問題ではある

発想

単調増加or 単調減少の数列のみで構成されるように区切る
1 2 3 2 1
1 2|3 2 1
1 2 3|2 1
..どっちの区切り方してもダイジョブ
1 2 1 2 3
1|2 1|2 3
1 2|1 2 3
...この場合は最小が存在する
...ただ、せいぜい2通り??? はじめを単調減少のみにするか、単調増加のみにするか????

 1  2  3  2  1
  +1 +1 -1 -1

 1  2  1  2  3
  +1 -1 +1 +1

 3  2  1  2  1
  -1 -1 +1 -1

長さN-1 のA_i,A_i+1 間の増減を記した配列Bを定義、
Bの種類を数え上げすればよさそう
##################################################### """
def check() :
    return


def main() :
    """ WA  
    A=1 2 2 1 の答えが1になる 
    

    """
    N = int(input())
    A = list(map(int, input().split()))
    B = [A[i]-A[i-1] for i in range(1,N)]
    result = 1
    i = 0
    while i < N-2 :
        if B[i]*B[i+1]<0 :
            result += 1
            i += 1
        i += 1
    print(result)
    return

def main2() :
    N = int(input())
    A = list(map(int, input().split()))
    B = [A[i]-A[i-1] for i in range(1,N)]
    result = 1
    i = 0
    while i < N-2 :
        if B[i]*B[i+1]<0 :
            result += 1
            i += 1
        elif B[i+1] == 0 :
            B[i+1] = B[i] #符号を引き継ぐ。0の場合はどっちにも対応できるの意味 
        i += 1
    print(result)
    return

if __name__ == "__main__" :
    main2()
    #check()
