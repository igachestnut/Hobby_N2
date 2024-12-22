def check() :
    return


def main() :
    N, C = map(int, input().split())
    T = list(map(int, input().split()))
    result = 1
    t = T[0]
    for i in range(1, N) :
        if T[i] - t >= C :
            #print(t)
            #print(T[i])
            #print()
            t = T[i]
            result += 1
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
