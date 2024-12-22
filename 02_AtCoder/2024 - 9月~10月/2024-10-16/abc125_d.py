def checker() :
    return


def main_my_old() :
    """ 次の配列は、選び方によって一定か逆転するか決まる。次の配列がそれぞれだった場合、現在までの経路で最大はどのようになるのかを記載するdpを作る。 """
    N = int(input())
    A = list(map(int, input().split()))

    dp = [A[0], -A[0]] #確定値。次の配列が1倍状態ならdp[0]、次の配列が逆転状態ならdp[1]に格納する
    for i in range(1, N-1) :
        # ある番号i において、次に取りうる最高の値というのは、
        # 次の状態がどのような結果になるかを考えると、
        # 次の状態が一定→ dp[0]の状態で無を選択する。dp[1]の状態で有を選択する。の二つである。
        # 逆に、次の状態が逆転→ dp[0]の状態で次を逆転選択する or dp[1]の状態でそのままを選択する　の２つである。
        dp = [max(dp[0]+A[i], dp[1]-A[i]), max(dp[0]-A[i], dp[1]+A[i])]
        # ただし、次の配列の状態が、入力のdp[]に正負が存在しない 0の場合がある。
        # その場合、..???直前までの経路で最大を選択できる 結局0 も、-1を選択した状態での0 と1を選択した状態での0を選べるのでは??

    print(max(dp))
    return

def main_old2() :
    """ 次の配列は、選び方によって一定か逆転するか決まる。次の配列がそれぞれだった場合、現在までの経路で最大はどのようになるのかを記載するdpを作る。 """
    N = int(input())
    A = list(map(int, input().split()))

    dp = [A[0], -A[0]] #確定値。次の配列が1倍状態ならdp[0]、次の配列が逆転状態ならdp[1]に格納する
    for i in range(1, N-1) :
        next_dp = [max(dp[0]+A[i], dp[1]-A[i]), max(dp[0]-A[i], dp[1]+A[i])]
        print(f"i:{i},dp{next_dp}")
        #dp = [ndp for ndp in next_dp]
    print(dp)
    print(max(dp[0]+A[-1], dp[1]-A[-1]))
    return

def main() :
    N = int(input())
    A = list(map(int, input().split()))

    dp = [A[0]+A[1], -A[0]-A[1], A[0]-A[1], -A[0]+A[1]] #無無→x1, 有有→x1, 無有→x-1, 有無→x-1
    for i in range(2, N-1) :
        dp = [max(dp[0]+A[i], dp[3]-A[i]), max(dp[1]+A[i], dp[2]-A[i]), max(dp[0]+A[i], dp[3]-A[i]), max(dp[1]+A[i], dp[2]-A[i])] #直前の選択を用いて、最大を定義する。
        print(dp)
    dp = [dp[0]+A[-1], dp[1]+A[-1], dp[2]-A[-1], dp[3]-A[-1]]
    print(dp)
    print(max(dp))
    

def main2() :
    N = int(input())
    A = list(map(int, input().split()))

    plus, minus, zero = 0, 0, 0
    for a in A :
        if a == 0 :
            zero += 1
            break
        elif a > 0 : plus += 1
        else : minus += 1

    abs_sumA = sum([abs(r) for r in A])
    if zero > 0 or minus % 2 == 0 :
        print(abs_sumA)
    else :
        min_abs_num = min([abs(r) for r in A])
        print(abs_sumA-min_abs_num*2)

if __name__ == "__main__" :
    main2()
    #checker()
