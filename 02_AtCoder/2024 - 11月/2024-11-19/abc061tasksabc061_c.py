""" #####################################################
発想


整数ai <= 10**5 より、1次元配列でなんの要素がどれだけの数入っているか格納できる。
計算量
- 格納→N 
- Kは一つしか計算しないので、配列の調査はO(10**5)
= O(N+10**5)


##################################################### """
def check() :
    return


def main() :
    N, K = map(int, input().split())
    A = [0 for i in range(10**5)]
    for i in range(N) :
        a, b = map(int, input().split())
        A[a-1] += b
    ruiseki = 0
    i = 0
    while ruiseki < K : #到達するまで実施する
        ruiseki += A[i]
        i+=1
    print(i)
    return


if __name__ == "__main__" :
    main()
    #check()
