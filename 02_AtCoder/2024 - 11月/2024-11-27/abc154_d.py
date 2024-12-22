""" #####################################################
発想

期待値
- あるさいころのMAX出目がpiだった時、考えられる期待値
    - pi = 4の時
        - 1/4*1 = 1/4
        - 1/4*2 = 2/4
        - 1/4*3 = 3/4
        - 1/4*4 = 4/4
        = 10/4  2.5
        = sum(1~4) / pi
    - piが偶数の時、(pi+1)*(pi/2) = 5*2 = 10
    - piが奇数の時、(pi+1)*(pi/2) = (3+1)*1.5 = 4*1.5=6
    ... (pi+1)*pi/2 /pi で期待値は求められる。O(1)

- 後は決められた連続の区間の最大合計期待値を計算したいので、
    尺取り法っぽく実装して、最大を(N-K)回だけ上書きすればよい


##################################################### """
def check() :
    return


def main() :
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ExpectedP = [(pi+1)/2 for pi in P]
    #print(ExpectedP)
    tmp_r = sum(ExpectedP[:K])
    result = tmp_r
    for i in range(K, N) :
        #print(tmp_r)
        tmp_r = tmp_r - ExpectedP[i-K] + ExpectedP[i]
        result = max(result, tmp_r)
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
