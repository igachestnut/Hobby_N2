def cheaker() :
    return


def main() :
    N = int(input())
    X = list(map(int,input().split()))

    X.sort()
    x = X[N:-N]
    print(sum(x)/(3*N))
    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
