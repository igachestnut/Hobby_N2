def cheaker() :
    return


def main() :
    """ 太郎君の得る最大の幸福値を出力する問題 
    
    MEMO
    ------------
    dpの構造
        そこまで(N = n)で選んだ値と最高値を保持したものを作成する。
        
        [[直前a],[直前b],[直前c],
         [     ],[    ],[     ],
         ,,,,,
        ]
    """
    N = int(input())
    
    #初期状態の値入力
    a, b, c = map(int, input().split())
    dp = [[a,b,c]]
    
    #直前のdpと比較し、最大値を記載したdpを作成する処理
    for n in range(N-1) :
        a, b, c = map(int, input().split())
        dp.append(get_maxpoint(a, b, c, dp))
        
    print(max(dp[-1]))        
    return

def get_maxpoint(a, b, c, dp) :
    now_a, now_b, now_c = dp[-1][0], dp[-1][1], dp[-1][2]
    new_a = max(now_b+a, now_c+a)
    new_b = max(now_a+b, now_c+b)
    new_c = max(now_a+c, now_b+c)
    return [new_a, new_b, new_c]
    


if __name__ == "__main__" :
    main()
    #cheaker()
