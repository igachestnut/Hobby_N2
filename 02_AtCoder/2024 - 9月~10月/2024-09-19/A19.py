""" ナップサック問題

  重さ 価値
i w_i v_i


"""
def cheaker() :
    return

def main() :
    N, W = map(int, input().split())
    dp = [0] + [-1 for i in range(W)] #0~W間のある重さj における最大の価値を定義する動的計画法配列
    for i in range(N) :
        w, v = map(int, input().split())
        for j in range(W, -1, -1) :
            if dp[j] != -1 and j+w <= W : dp[j+w] = max(v+dp[j], dp[j+w])
    print(max(dp))
    return

if __name__ == "__main__" :
    main()
    #cheaker()
