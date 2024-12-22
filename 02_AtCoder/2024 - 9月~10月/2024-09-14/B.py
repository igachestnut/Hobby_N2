def cheaker() :
    return


def main() :
    N, M = map(int, input().split())
    born_flag = [False for i in range(N+1)]
    for m in range(M) :
        a, b = input().split()
        if born_flag[int(a)] == False and b == "M" :
            print("Yes")
            born_flag[int(a)] = True
        else :
            print("No")
    return


if __name__ == "__main__" :
    main()
    #cheaker()
