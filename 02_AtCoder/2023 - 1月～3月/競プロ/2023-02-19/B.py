def cheaker() :
    return


def main() :
    N,K = map(int,input().split())
    S = list(input())
    for i in range(N) :
        if S[i] == "o" and K > 0 :
            K -= 1
            pass
        elif K == 0 :
            S[i] = "x"

    T = "".join(S)
    print(T)

    return


if __name__ == "__main__" :
    main()
    #cheaker()
