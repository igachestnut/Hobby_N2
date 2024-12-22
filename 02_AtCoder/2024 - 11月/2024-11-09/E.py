""" ########################
10進法で定義される文字列を総和をだせ
all substring

- 連続部分文字列の問題
定義できる文字列の種類? 総数
f(i, j) 
i が1の時、j が1~Nまで実行される。
この際、i の倍率というのは、i, i*10, i*10**2, ...のように増えていくだろう
答え = iにおける総数 = S[i]*

i+10i+100i 
111i = 
ただし、計算に2*10**5桁の数値で計算しようとすると、
int型ではメモリが足りない→ある程度工夫が必要そうであろう。

桁が値を確定していく感じ?
dp[0] = 0
dp[1] = dp[0] + S[i]
dp[i+1] = dp[i] + S[i+1]
繰り上がった数値をstrの上のほうに加算していく?

dpを全定義。
下から値を確定していく。

1. dpで値を計算

いやいやちょっと違かった。
i=1の時
答え
111i

i=2の時
答え
22i

である。

####################### """
def check() :
    return


def main() :
    N = int(input())
    S = input()

    dp = [0]
    for i,s in enumerate(S) :
        dp.append(dp[-1]+int(s)*(i+1))
    
    result = []
    tmp_r = 0
    for r in dp[::-1]: #逆から値を確定していく。
        tmp_r += r
        result.append(tmp_r%10)
        tmp_r = tmp_r//10

    if result[-1] == 0: result.pop(-1)
    print("".join(map(str, result[::-1])))
    return


if __name__ == "__main__" :
    main()
    #check()
