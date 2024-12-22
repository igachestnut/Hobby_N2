def check() :
    return


def main() :
    N, c1,c2 = input().split()
    S = input()
    result = ""
    for i in range(int(N)) :
        if c1 != S[i] :
            result += c2
        else :
            result += c1
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
