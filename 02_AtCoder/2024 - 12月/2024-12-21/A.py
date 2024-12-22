def check() :
    return


def main() :
    A,B,C = map(int, input().split())
    if A==B==C :
        print("Yes")
    elif A == B+C or B ==A+C or C==A+B:
        print("Yes")
    else :
        print("No") 
    return


if __name__ == "__main__" :
    main()
    #check()
