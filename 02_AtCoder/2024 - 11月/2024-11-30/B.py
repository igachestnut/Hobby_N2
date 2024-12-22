def check() :
    return


def main() :
    N,D = map(int, input().split())
    S=list(input())
    i = -1
    while D > 0:
        if S[i] == "@" :
            S[i] = "."
            D -=1
        i -=1
    print("".join(S))
    return


if __name__ == "__main__" :
    main()
    #check()


if __name__ == "__main__" :
    main()
    #check()
