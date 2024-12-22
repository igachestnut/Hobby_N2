def cheaker() :
    return


def main() :
    N, X, Y, Z = map(int, input().split())
    
    if X < Z < Y or Y < Z < X :
        print("Yes")
    else :
        print("No")
    return


if __name__ == "__main__" :
    main()
    #cheaker()
