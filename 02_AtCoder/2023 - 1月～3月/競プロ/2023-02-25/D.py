def cheaker() :
    return


def main() :
    from collection import deque

    N = int(input())
    X = list(map(int,input().split()))

    X.sort()
    x = X[N:-N]
    print(x)
    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
