def check() :
    return


def main() :
    N,D = map(int, input().split())
    S=input()
    result = D
    for s in S: 
        if s==".": result+=1
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
