def cheaker() :
    return


def main() :
    N,M = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    ans = 0
    for i in b :
        ans += a[i-1]
        
    print(ans)
    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
