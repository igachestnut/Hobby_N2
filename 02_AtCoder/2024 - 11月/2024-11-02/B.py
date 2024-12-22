def check() :
    return


def main() :
    N = int(input())
    callender = []
    for i in range(N) :
        callender.append(list(map(int, input().split())))
    Q = int(input())
    for q in range(Q) :
        t, d = map(int,input().split())
        if (d-callender[t-1][1]) % callender[t-1][0] == 0 :
            m = (d-callender[t-1][1]) //callender[t-1][0] 
        else :
            m = (d-callender[t-1][1]) //callender[t-1][0] +1
        print(callender[t-1][0]*m + callender[t-1][1])
    return


if __name__ == "__main__" :
    main()
    #check()
