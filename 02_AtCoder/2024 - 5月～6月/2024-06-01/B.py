def cheaker() :
    return


def main() :
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    
    for i in range(N) :
        X = list(map(int, input().split()))
        for j in range(M) :
            A[j] -= X[j]
        
    if max(A) <= 0 :
        print("Yes")
        return
    else :
        print("No")
        return 
                  
    return


if __name__ == "__main__" :
    main()
    #cheaker()
