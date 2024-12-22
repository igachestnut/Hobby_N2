def cheaker() :
    return


def main() :
    N = int(input())
    SC = {}
    
    for n in range(N) :
        s, c = input().split()
        SC[str(s)] = int(c)
    
    sorted_SC = sorted(SC.keys())
    #計算
    T = sum(SC.values()) % N
    #print(SC)
    #print(sorted_SC)
    print(sorted_SC[T])
    return


if __name__ == "__main__" :
    main()
    #cheaker()
