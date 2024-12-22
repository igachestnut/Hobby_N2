def cheaker() :
    return


def main() :
    N = int(input())
    A, B = [], []
    for n in range(N) :
        A.append(list(input()))
    for n in range(N) :
        B.append(list(input()))

    #print(A)
    for ny in range(N) :
        for nx in range(N) :
            if A[ny][nx] != B[ny][nx] :
                print(ny+1, nx+1)
                return
            
    return


if __name__ == "__main__" :
    main()
    #cheaker()
