def cheaker() :
    return


def main() :
    N,K = map(int,input().split())
    S = [input() for _ in range(N)]
    ans = S[:K]
    ans.sort()
    for i in range(len(ans)) :
        print(ans[i])
    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
