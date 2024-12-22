def cheaker() :
    return


def main() :
    N = int(input())
    shoud_change = [False for i in range(N*(N-1)//2)] #辺が存在しない位置は全て作業する必要がない。のでFalse
    mymap = [[-1 for j in range(N+1)] for i in range(N+1)]
    #print(mymap)

    id = 0 
    for i in range(1, N) :
        for j in range(i+1, N+1) :
            mymap[i][j] = id
            id += 1
    print(mymap)

    MG = int(input())
    for i in range(MG) :
        u, v = map(int, input().split())
        shoud_change[mymap[u][v]] = True #変更が必要になる箇所をTrueに

    MH = int(input())
    for i in range(MH) :
        a, b = map(int, input().split())
        shoud_change[mymap[a][b]] = False if shoud_change[mymap[a][b]] == True else True #既に橋が存在しているならば、入力は正しくなるため、False(変える必要が無いもの)とする

    A = []
    for i in range(N-1) : 
        tmp_a = list(map(int, input().split()))
        for a in tmp_a : A.append(a)

    print(shoud_change)
    print(A)
    result = 0
    for i in range(len(shoud_change)) :
        result += shoud_change[i] * A[i]
    print(result)
    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
