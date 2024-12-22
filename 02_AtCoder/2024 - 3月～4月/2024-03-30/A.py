def cheaker() :
    return


def main() :
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    result = ""
    for i in range(N) :
        if A[i] % K == 0 and A[i] != 0 :
            result += str(A[i] // K) + " "
    print(result)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
