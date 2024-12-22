def cheaker() :
    return


def main() :
    N = int(input())
    H = list(map(int, input().split()))
    
    result = -1
    for n in range(N) :
        if H[0] < H[n] :
            result = n+1
            break
    
    print(result)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
