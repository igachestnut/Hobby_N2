def cheaker() :
    return


def main() :
    N = int(input())
    X = list(map(int, input().split()))
    myX = [x for x in X]
    ans = []

    #中央値の導出
    myX.sort()
    mid1, mid2 = myX[N//2-1], myX[N//2]
    for i in range(N) :
        if X[i] <= mid1 : ans.append(mid2)
        else : ans.append(mid1)
    
    for a in ans :
        print(a)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
