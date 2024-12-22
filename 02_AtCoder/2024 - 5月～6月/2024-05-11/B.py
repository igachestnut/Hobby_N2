def cheaker() :
    return


def main() :
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    # 何回でアトラクションが終わるのかを計測する
    action_count = 0
    while A : #Aが無くなるまで実行する
        k = K #空席
        while A and k >= A[0] : #空席kに人を入れられる場合に実行
            a = A.pop(0)
            k -= a
        action_count += 1
    
    print(action_count)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
