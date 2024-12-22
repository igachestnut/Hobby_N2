def cheaker() :
    return


def main() :
    N = int(input())
    A = []
    for i in range(N) :
        A.append(list(map(int, input().split())))
    
    tmp_alchemy = 0
    for i in range(N) :
        tmp_alchemy = A[tmp_alchemy][i] -1 if tmp_alchemy >= i else A[i][tmp_alchemy] -1
    
    print(tmp_alchemy+1)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
