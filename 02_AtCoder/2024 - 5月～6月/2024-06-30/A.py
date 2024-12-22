def cheaker() :
    return


def main() :
    S = list(input())
    
    for s in S :
        if "R" == s :
            print("Yes")
            return
        elif "M" == s :
            print("No")
            return
        else :
            pass
    return


if __name__ == "__main__" :
    main()
    #cheaker()
