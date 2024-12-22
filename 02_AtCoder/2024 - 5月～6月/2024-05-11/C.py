def cheaker() :
    return


def main() :
    N = int(input())
    A = list(map(int, input().split()))
    
    result = 0
    for a in A :
        result += (a * (N-1)) % (10**8)
    
    print(result % (10 ** 8))
    
    return

def main2() :
    """ 問題の肝
    
    計何回割る回数が生じるのかを探索すると、答えが出る。
    xn (1~N)において、別の文字を探索した結果、
    10^8を超える数がどこまでなのかというのを2分探索で導出したら答えが出そう。
    
    
    
    """
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    
    count = 0
    # NlogNで超えるカウントを行う
    for n in range(N-1) :
        # 計算した結果超える位置はどこなのかを二分探索で調査
        # 超える場所での（10^8をする数値）での最大位置を_max(index)と指定
        _max, _min = N-1, n+1
        
        # 超える位置の特定がすむまで実行
        while _max != _min :
            tmp = (_max + _min) // 2
            if A[n] + A[tmp] >= 10**8 :
                _max = tmp
            else :
                _min = tmp + 1
        
        # もしすべての数値が超えていない場合のスルー
        if A[n] + A[_min] < 10**8 : #算出した値が超えていない場合
            #print(f"index{n}において、超える計算をさせなきゃならない合計は0回だった")
            continue
        else :
            count += N-1-(_max-1) #超えない位置を除外させる。
        #print(f"index{n}において、超える計算をさせなきゃならない合計は{N-1-(_max-1)}回だった")

    # 値の全計算
    result = 0
    for a in A :
        result += a * (N-1)
    
    result -= count*(10**8)
    print(result)
            
    return



if __name__ == "__main__" :
    main2()
    #cheaker()
