""" #####################################################
発想


- お湯の出る総和。
- T = 5
    t = [1,10,11]の時
    1~5 10~11~16 までお湯が出る。
    t1 が押された時点で、答えの最大数 = T
    t2 が押されえた時点で、答えの最大数 += T-max(t1+T-t1, 0) #あまり時間だけ削除する
##################################################### """
def check() :
    return


def main() :
    N, T = map(int, input().split())
    time_log = list(map(int, input().split()))
    result = T #1回以上は必ず押されるため
    for i in range(1, N) :
        result += T-max(time_log[i-1]+T-time_log[i], 0)
    
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
