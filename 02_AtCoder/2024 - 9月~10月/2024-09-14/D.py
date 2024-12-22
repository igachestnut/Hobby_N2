import bisect
def cheaker() :
    return


def main() :
    N = int(input())
    X = list(map(int, input().split()))
    P = list(map(int, input().split()))

    ruiseki_P = [0]
    for p in P : ruiseki_P.append(ruiseki_P[-1] + p)
    
    Q = int(input())
    for i in range(Q) :
        L, R = map(int, input().split())
        i = bisect.bisect_left(X, L)
        j = bisect.bisect(X, R)
        print(ruiseki_P[j]-ruiseki_P[i])
    return


if __name__ == "__main__" :
    main()
    #cheaker()
