def cheaker() :
    return


def main() :
    N, Q = map(int, input().split())
    T = list(map(int, input().split()))
    
    # 歯の生えている場所
    tooth = [True for i in range(N)]
    for t in T:
        if tooth[t-1] :
            tooth[t-1] = False
        else :
            tooth[t-1] = True
    
    print(sum(tooth))
    return


if __name__ == "__main__" :
    main()
    #cheaker()
