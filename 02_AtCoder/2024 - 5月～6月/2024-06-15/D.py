def cheaker() :
    return


def main() :
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    
    # 低い順にBを見ていって、一番安いものを買い続ける手法。若干尺取り法っぽいけどちょっと違うやり方 計算量O(N+M)
    # Mの最低を見る
    n, m = 0, 0
    result = 0
    
    #お土産を買う必要のある人間が終了するまで実行
    while m < M :
        #Biさんの土産を決定するまで実行
        if n >= N : #もしすべての買える手段が尽きたとき。（尽きているとき）
            print("-1")
            return
        
        # 現在の着目しているお土産を見て、買える時 (与えたい人 <= 買えるお土産(条件成立))
        if B[m] <= A[n] :
            result += A[n] #購入処理
            n += 1 #買えたんで次のお土産
            m += 1 #買えたんで次の人
        else : #買えない時、次のお土産に着目する。
            n += 1
           
    print(result)    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
