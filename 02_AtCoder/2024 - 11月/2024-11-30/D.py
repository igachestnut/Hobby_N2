def check() :
    return


def main() :
    """ 一つ一つ固定して出力していく """
    N, M = map(int, input().split())
    result = [1+10*i for i in range(N)]
    play = True
    while play :
        print(*result)
        for j in range(result[-1], M) :
            result[-1]+=1
            print(*result)
        
        for k in range(N-2, -2, -1):
            if k==-1 :
                play = False
                break
            if result[k]+10 == result[k+1] :
                continue
            else :
                result[k] += 1
                for l in range(k+1, N) :
                    result[l] = result[l-1]+10    
    return

def main2() :
    """ 一つ一つ固定して出力していく """
    N, M = map(int, input().split())
    result = [1+10*i for i in range(N)]
    play = True
    while play :
        for j in range(result[-1], M+1) :
            result[-1] = j
            print(*result)
        
        for k in range(N-1, -1, -1):
            if k==0 :
                play = False
                break
            if result[k-1]+10 == result[k] :
                continue
            else :
                result[k-1] += 1
                for l in range(k, N) :
                    result[l] = result[l-1]+10    
                break
    
    return

def main3() :
    """ 一つ一つ固定して出力していく 
    
    in
    12 120 
    out 
    293930

    このout (X)を計算で(できればO(N or 1))で出す方法はないだろうか?

    ...あと、最大数が293930 通りなので、results配列を作るのに必要な処理量 293930*12 で3 *10**7 となる。
    """
    N, M = map(int, input().split())
    result = [1+10*i for i in range(N)]

    play = True
    results = []
    while play :
        for j in range(result[-1], M+1) :
            result[-1] = j
            #print(*result)
            results.append([r for r in result])
        
        for k in range(N-1, -1, -1):
            if k==0 :
                play = False
                break
            if result[k-1]+10 == result[k] :
                continue
            else :
                result[k-1] += 1
                for l in range(k, N) :
                    result[l] = result[l-1]+10    
                break
    print(len(results))
    for r in results:
        print(*r)
    return



if __name__ == "__main__" :
    main3()
    #check()
