def check() :
    return


def main() :
    lis = list(map(int, input().split()))
    lis.sort()
    syurui = len(set(lis))
    if syurui == 2 :
        print("Yes")
    else :
        print("No")
    return


if __name__ == "__main__" :
    main()
    #check()
