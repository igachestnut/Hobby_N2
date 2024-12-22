def checker() :
    print(2**20 < 10**8)
    return


def main() :
    N = int(input())
    K = list(map(int, input().split()))

    B_maxlen = sum(K)//2
    dp = [-1 for i in range(B_maxlen+1)]
    dp[0] = 0
    for k in K :
        for i in range(B_maxlen, -1, -1) :
            if dp[i] != -1 and i+k <= B_maxlen : dp[i+k] = dp[i] + k
    #print(dp)
    for i in range(B_maxlen, -1, -1) :
        if dp[i] != -1 :
            print(sum(K) - dp[i])
            return
    return

def main2() :
    """ 情報を選択するか否かを決める """
    N = int(input())
    K = list(map(int, input().split()))

    queue = [0]
    for k in K :
        new_queue = []
        for que in queue :
            new_queue.append(que+k)
        for oq in queue : new_queue.append(oq)
        queue = new_queue
    #print(queue)
    B_len_max = sum(K)/2
    result = sum(K)
    for q in queue : 
        if B_len_max <= float(q) : result = min(result, q)
    print(result)

if __name__ == "__main__" :
    main2()
    #checker()
