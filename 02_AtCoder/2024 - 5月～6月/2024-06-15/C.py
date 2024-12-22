def cheaker() :
    return


def main() :
    N, M = map(int, input().split())
    S =  []
    for i in range(N) :
        tmp_s = list(input())
        S.append([True if s == "o" else False for s in tmp_s])
    #print(S) #リストの中身確認
    
    #BFSを用いた探索。
    result = 0
    ans = tuple([True for j in range(M)])
    queue = set()
    queue.add(tuple([False for j in range(M)]))
    #もし前回の探索結果(ありうる全ての買えたポップコーンの組み合わせ)の中に、全てTrueがあるならば。終了
    #print(ans)
    #print(queue)
    while ans not in queue :
        #全ての組み合わせの調査の開始
        new_queue = set()
        for que in queue :
            for tmp_s in S :
                new_que = tuple([a or b for a, b in zip(que, tmp_s)])
                new_queue.add(new_que)
        queue = new_queue
        result += 1
        #print(queue)
    
    
    print(result)
                    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
