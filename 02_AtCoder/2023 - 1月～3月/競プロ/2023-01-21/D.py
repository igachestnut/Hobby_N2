

def DP(X,coin) :
    
    dp = [[0 for i in range(X)] for j in range(len(coin))]

    #一列目
    for i in range(X) :
        if i >= coin[0] :
            dp[0][i] = coin[0]

    #二列目以降
    for j in range(1,len(coin)) :
        for i in range(X) :
            if i < coin[j] :
                dp[j][i] = dp[j-1][i]
            else :
                dp[j][i] = max(coin[j] + dp[j-1][i-coin[j]] , dp[j-1][i])

    if dp[-1][-1] == X :
        return "Yes"
    else :
        return "No"

N,X = map(int,input().split())
coin = []
for n in range(N) :
    a,b = map(int,input().split())
    tmp = [a for _ in range(b)]
    coin += tmp


print(DP(X,coin))


#時間制限切れで答えられなかった。
#時間切れ3分後にACをとった。

#敗因？教訓？
#dpグラフを作る際に0の情報を入れ忘れていたこと。
#dpのrangeをiはXまでとしてしまっていた。
#逆にrange(X) = 0～X-1までとしてしまっていた。
#⇒iを「0」～「X」にするべきだった。そうすると定量的に扱える。
#　多分他の動的計画法も同じ感じなので、やるようにしましょう。

#ただし、考え方自体は非常によく、ほぼ問題なく実装できた。
#また、この問題がDPと気づくまでかかった時間がとても短く、成長を感じた。

"""
学び
・動的計画法は値の大きさ関係なく最大値を求めることができる！
　（coin.reverseなくてもいい！）
・pypy3とpython3の実行時間の差を調べた
　python3ではTLEとなってしまった。
　pypy3では問題なく、あと4倍程度の負荷までかけられそうではあった。

・動的計画法の難しさの発見
　・定量的に扱うためにdpのリストを「0」から定義すること。
　　　（プログラム中は完全に頭から抜けてました。）




"""
