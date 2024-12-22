def cheaker() :
    return


def main() :
    N, S = map(int, input().split())
    A = list(map(int, input().split()))
    
    dp = [[] for i in range(S+1)] #dp その位置iにおいて、可能な組み合わせをリストとして記載するdp
    for i in range(N) :
        for j in range(S, -1, -1) :
            if dp[j] != [] and j + A[i] <= S and dp[j+A[i]] == [] : 
                for d in dp[j] : dp[j+A[i]].append(d)
                dp[j+A[i]].append(i+1)
        if A[i] <= S and dp[A[i]] == []:
            dp[A[i]].append(i+1)
        #print(dp)
        #print(i)
        #print("---------------------------")
    #print(dp)
    
    if dp[-1] != [] :
        print(len(dp[-1])) 
        print(*dp[-1])
    else : print(-1)    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
