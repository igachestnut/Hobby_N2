""" #####################################################
発想

- HW行のマス  
- 上からr, 左からc

- .が白色, #が黒色

- 2次元DPを考える、
- 遷移を考える。
    - dp[0,0] 
        - 白色ならそのままでよい。ひっくり返す回数は0回。
        - 黒色ならひっくり返す必要がある。dp[0,0]において最小ひっくり返す回数=1回。
    - dp[i+1,j]  (or dp[i, j+1])
        - dp[i,j]と、dp[i+1,j]がもし同じNodeだった場合、
        今までの最小ひっくり返された数値がdp[i,j]=1 回なら、それに合わせてdp[i+1,j]も一緒にひっくり返せばよい。
        すると、dpの現在と移動後の色が一緒ならひっくり返さなくてもよいので、数値を引き継ぐことができる。
        - 逆に異なる数値の場合。
        新規にひっくり返す必要があるもしくは、今までのNodeをひっくり返してそのままの状態で

    ...ある経路を白色にしたいので、黒が新規に見えたとき、新規にひっくり返す必要がありそう。
    →今は"." 次は"#" の時だけ値をプラスする。 今は#, 次は. の時は値は変える必要がない。

    ..2次元DPの特徴だが、一番上の行は横移動のみで最高率を出せ、一番左の列 は縦移動のみで最高率を出せる。
    - それらを用いて、上左から値を引き継ぐ感じ。

##################################################### """
def check() :
    return


def main() :
    H,W = map(int, input().split())
    S = [list(input()) for i in range(H)]

    dp = [[float("inf") for j in range(W)] for i in range(H)]

    #print(S)
    # DP 初期化処理。一番上の行、一番左の行の最高率を求める
    if S[0][0] == "." :
        dp[0][0] = 0 
    else :
        dp[0][0] = 1
    for i in range(H-1): 
        if S[i][0] == "." and S[i][0] != S[i+1][0]: #.→#の境界が見えるとき 
            dp[i+1][0] = dp[i][0]+1 
        else :
            dp[i+1][0] = dp[i][0]
    for j in range(W-1) :
        if S[0][j] == "." and S[0][j] != S[0][j+1]: #.→#の境界が見えるとき 
            dp[0][j+1] = dp[0][j]+1 
        else :
            dp[0][j+1] = dp[0][j]
    #print(dp)

    # 2次元DP 上、左から値を引き継ぐ
    for i in range(1, H) :
        for j in range(1, W) :
            tr,tc = dp[i-1][j], dp[i][j-1]
            if S[i-1][j] == "." and S[i-1][j] != S[i][j] :
                tr += 1
            if S[i][j-1] == "." and S[i][j-1] != S[i][j] :
                tc += 1
            dp[i][j] = min(tr, tc)
    #print(dp)
    print(dp[-1][-1])
    return


if __name__ == "__main__" :
    main()
    #check()
