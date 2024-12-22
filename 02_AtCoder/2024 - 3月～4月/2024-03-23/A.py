def cheaker() :
    return


def main() :
    N = int(input())
    a = list(map(int, input().split()))
    
    b = ""
    for i in range(N-1) :
        b += str(a[i]*a[i+1]) + " "
        
    print(b)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
