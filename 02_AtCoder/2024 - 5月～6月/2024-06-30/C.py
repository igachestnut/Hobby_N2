def cheaker() :
    return


def main() :
    """ 箱量＋荷物数が同じであることより、重なった荷物は、必ず小さいほうから分割すればよい。"""
    N = int(input())
    max_weight = [0 for i in range(N)] #最小要領を記載するもの
    
    A = list(map(int, input().split()))
    W = list(map(int, input().split()))
    
    result = 0
    for i in range(N) :
        if max_weight[A[i]-1] < W[i] :#現在着目している荷物の方が重そうであると判断する場合
            result += max_weight[A[i]-1]
            max_weight[A[i]-1] = W[i]
        else :
            result += W[i]
    
    print(result)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
