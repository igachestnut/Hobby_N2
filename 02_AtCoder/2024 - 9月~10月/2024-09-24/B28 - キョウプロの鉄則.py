def cheaker() :
    return


def main() :
    N = int(input())
    A = [1 for i in range(N+1)]
    for i in range(3, N+1) :
        A[i] = (A[i-1] + A[i-2] ) % 1000000007
    print(A[N])
    return


if __name__ == "__main__" :
    main()
    #cheaker()
