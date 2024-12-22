def cheaker() :
    return

# 動的計画法を用いた、最大スコア算出
def main() :
    N = int(input())
    A = list(map(int, input().split()))
    score = [0, 0] #選択時のスコア 左が次1倍で、右が次二倍スコアを選択できる。
    for i in range(N) :
        #print(score)
        if i == 0 :
            score[1] = A[i]
            continue
        next_s0 = max(score[0], score[1] + A[i]*2)
        next_s1 = max(score[1], score[0] + A[i])
        score = [next_s0, next_s1]
    print(max(score))
    return

if __name__ == "__main__" :
    main()
    #cheaker()
