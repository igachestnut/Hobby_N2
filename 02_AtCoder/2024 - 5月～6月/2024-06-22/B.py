def cheaker() :
    return


def main() :
    N = int(input())
    A = list(map(int, input().split()))
    result = 0
    for i in range(2, 2*N) :
        before = A[i-2]
        if before == A[i] :
            result += 1
    print(result)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
