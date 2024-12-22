def cheaker() :
    return


def main() :
    N, L, R = map(int, input().split())
    A = [n+1 for n in range(N)]
    reverse_array = A[L-1:R]
    reverse_array.reverse()
    A[L-1:R] = reverse_array
    print(*A)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
