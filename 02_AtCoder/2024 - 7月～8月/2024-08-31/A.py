def cheaker() :
    return


def main() :
    A, B = map(int, input().split())
    result = 0
    if A == B :
        print(1)
        return
    if (A+B) % 2 == 0 :
        print(3)
    else :
        print(2)   
    return


if __name__ == "__main__" :
    main()
    #cheaker()
