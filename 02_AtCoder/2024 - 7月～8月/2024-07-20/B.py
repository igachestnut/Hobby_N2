def cheaker() :
    return


def main() :
    N, T, P = map(int, input().split())
    L = list(map(int, input().split()))
    
    for i in range(0, 100) :
        count = 0
        for j in range(N) :
            if L[j] +i >= T :
                count += 1
        if count >= P:
            print(i)
            return
    return


if __name__ == "__main__" :
    main()
    #cheaker()
