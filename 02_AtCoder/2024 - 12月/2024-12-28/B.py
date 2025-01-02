def check() :
    return


def main() :
    S = input()
    result = 0
    i = 0
    while i < len(S) :
        if S[i] == "0" :
            if i+1 < len(S) and S[i+1] == "0" :
                i += 1
        result += 1
        i += 1
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
