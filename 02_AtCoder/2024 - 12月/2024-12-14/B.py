def check() :
    return


def main() :
    N, R = map(int,input().split())
    for i in range(N) :
        D, A = map(int, input().split())
        if D == 1 :
            if 1600 <= R < 2800 :
                R = R+A
            else :
                pass
        else :
            if 1200<= R < 2400:
                R = R+A
            else :
                pass
    print(R)
    return


if __name__ == "__main__" :
    main()
    #check()
