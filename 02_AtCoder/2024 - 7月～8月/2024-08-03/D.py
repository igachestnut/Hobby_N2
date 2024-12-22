"""  

発想

最大の勝率＝直前までの最大と、終了状況でしかない。
    R, S, P
dp [最大勝率, 最大勝率, 最大勝率]


"""

def cheaker() :
    return


def main() :
    N = int(input())
    S = list(input())
    
    #dpの初期化 dp:#R S P をそれぞれ選択した時の最大勝利数
    if S[0] == "R" :#グー
        dp = [0, -1, 1]
    elif S[0] == "S" :#チョキ
        dp = [1, 0, -1]
    else :#パー
        dp = [-1, 1, 0]

    for i in range(1, N) :
        if S[i] == "R" :#グー
            #index0であいこ
            max_dp0 = max(dp[1], dp[2])
            #index2で勝ち
            max_dp2 = max(dp[0], dp[1]) +1
            new_dp = [max_dp0, -1, max_dp2]   
        elif S[i] == "S" :#チョキ
            #index0で勝ち
            max_dp0 = max(dp[1], dp[2]) +1
            #index1であいこ
            max_dp1 = max(dp[0], dp[2])
            new_dp = [max_dp0, max_dp1, -1]   
        else :
            #index1で勝ち
            max_dp1 = max(dp[0], dp[2])+1
            #index2であいこ
            max_dp2 = max(dp[0], dp[1])
            new_dp = [-1, max_dp1, max_dp2]   
        dp = new_dp  
    print(max(dp))      
    return


if __name__ == "__main__" :
    main()
    #cheaker()
