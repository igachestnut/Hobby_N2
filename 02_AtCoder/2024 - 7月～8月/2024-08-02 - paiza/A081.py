def cheaker() :
    return


def main() :
    N = int(input())
    start_i = [-1 for i in range(N)]
    result = 0
    for i in range(2*N) :
        a = int(input())
        if start_i[a-1] == -1 :
            start_i[a-1] = i+1
        else :
            result += abs((i+1) -start_i[a-1] -1) #現在検知した値から、初めて見つけた位置を引く。例)i, i+1なら0になる。
    print(result)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
