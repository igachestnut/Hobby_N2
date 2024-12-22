def cheaker() :
    return


def main() :
    s = list(input())
    ans = []
    for i in range(len(s)) :
        if s[i] == "1" :
            ans.append(str(0))
        else :
            ans.append(str(1))

    print("".join(ans))
    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
