def cheaker() :
    return


def main() :
    N = int(input())
    A = list(map(int, input().split()))
    B = [a for a in A] 
    B.sort()
    for i in range(N) :
        if B[-2] == A[i] :
            print(i+1)
            return
        
    return


if __name__ == "__main__" :
    main()
    #cheaker()
