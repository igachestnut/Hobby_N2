""" #####################################################
発想

- 任意の要素の和は、K以上である。

- 1 2 2 2 1  K=3の時、
- l=1,r=2以上の時、必ずTrue

- 連続する部分文字列の列挙方法
N + N-1 ,,,, 1
= N(N+1)//2 
....尺取り法で解く。
##################################################### """
def check() :
    return


def main() :
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    result = N*(N+1)//2

    r = 0
    tmp_sum = 0
    for l in range(N) :
        if l > r : 
            r = l
            tmp_sum = 0

        while r < N and tmp_sum+A[r] <K:
            tmp_sum += A[r] 
            r += 1

        result -= r-l
        tmp_sum -= A[l]
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
