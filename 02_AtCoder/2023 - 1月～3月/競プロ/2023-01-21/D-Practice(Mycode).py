def DP(X,coin) :
    #リストの作成
    dp = [[0 for i in range(X+1)] for j in range(len(coin))]

    #一列目
    for i in range(X+1) :
        if i >= coin[0] :
            dp[0][i] = coin[0]

    #二列目以降
    for j in range(1,len(coin)) :
        for i in range(X+1) :
            if i < coin[j] :#コインの重みが超えるまでスキップ
                dp[j][i] = dp[j-1][i]#上から持ってくるだけ
            else :
                dp[j][i] = max(coin[j] + dp[j-1][i-coin[j]] , dp[j-1][i])

    #条件ごとで判定する。
    if dp[-1][-1] == X :
        return "Yes"
    else :
        return "No"


def main() :
    N,X = map(int,input().split())
    coin = []
    for n in range(N) :#リストの作成。今回はコイン硬化全てをバラバラに考えた。
        a,b = map(int,input().split())
        tmp = [a for _ in range(b)]
        coin += tmp
    print(DP(X,coin))


if __name__ == "__main__" :
    main()
