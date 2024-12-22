def cheaker() :
    return


def main() :
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = A[-K:] + A[:N-K]
    print(*B)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
