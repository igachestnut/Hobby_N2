def check() :
    return


def main() :
    S = input()
    result = []
    count = 0
    for i in range(len(S)) :
        if S[i] == "|" :
            result.append(count)
            count = 0
        else :
            count+=1
    print(*result[1:])
    return


if __name__ == "__main__" :
    main()
    #check()
