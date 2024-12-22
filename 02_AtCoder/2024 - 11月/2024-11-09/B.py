def check() :
    return


def main() :
    N, K = map(int, input().split())
    S = input()
    result = 0
    ok = 0
    for i in range(N) :
        if S[i] == "O" :
            ok +=1
            if ok == K :
                result += 1
                ok = 0
        else :
            ok = 0
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
