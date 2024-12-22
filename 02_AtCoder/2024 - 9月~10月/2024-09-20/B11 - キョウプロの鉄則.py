def cheaker() :
    return


import bisect

def main() :
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    
    Q = int(input())
    for q in range(Q) :
        x = int(input())
        result = bisect.bisect(A, x-1)
        print(result)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
