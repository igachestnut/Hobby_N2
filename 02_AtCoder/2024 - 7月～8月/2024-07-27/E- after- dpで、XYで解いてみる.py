""" #####################################################
発想

動的計画法を用いた解法
XYで解いてみる。10000以内で存在しそうな話を


##################################################### """
#import memory_profiler as MP
#import gc
#import random
    
def cheaker() :
    """ メモリ使用量をチェックしようのコーナー
    
    MEMO
    --------
    - Nodeとint が入ったデータの使用量を確認してみる
    
    - 条件
        1. 3次元配列 10**2 * 10**2 * 10 
        2. int or None
        - 結果
            1. int(0)だったら→1.9375[MB]
            2. None → 1.9296875[MB]
            3. float(0) → 5.08203125[MB]
            4. float("inf") → 5.0546875[MB]
            5. [None] → 9.65625[MB]
            
    - 条件2
        1. 2次元配列 10**5 * 80 
        2. int or None
        - 結果(条件2より)
            1. int(0) → 61.94921875 [MB]
            2. None → 61.93359375 [MB]
        
    -----------------
    - 結論
        1. Noneとint型変数が使用するメモリ量は同じくらい
        2. Listを囲いとして導入するとメモリ使用量は10倍になる。
        3. 容量の関係もあるが、オブジェクト数は合計で10**7以内くらいには抑えたい。
    """
    b1 = MP.memory_usage()[0]
    dp = [[None for j in range(10**5)]for k in range(80)]
    b2 = MP.memory_usage()[0]
    print(b2 - b1, "[MB]")
    return


def main() :
    """ 発想
    
    Nodeをどんどん追加していくアルゴリズム。
    - db構造について
        1. 2次元構造 k * X(1~10*4+1)まで
        2. 初期状態では、全て-1が代入され、[0][0]だけ0
        3. k, Xは1~Xを含む0~Xのデータ構造とする。(0を余分に追加することとする。)
        4. 記載する値は、しょっぱさの(Y)の最小値
            - d[k][x] その一に格納されている値は、d[k][x]という最小しょっぱさであり、xの甘さで構成され、k個のNodeによって構成されている
        
    1. 1,2,,,,i N について実行。(一つ一つNodeを追加)
    2. 最も多い階層kから1行ずつ実行。該当するオブジェクトが存在する場合,(-1)ではない場合、そこから次へのNodeを追加する。
    
    """
    N, X, Y = map(int, input().split())
    d_map = [[Y+1 for x in range(X+1)] for k in range(N+1)]
    d_map[0][0] = 0 #k(選ばれていない⋀、価値無しの原点を置く)
    
    #処理の実行
    for i in range(N) :
        a, b = map(int, input().split())
        #print("-----------------------------------------")
        #print(d_map)
        for k in range(i, -1, -1) : #逆順に実行
            #print(f"{i},i")
            for x in range(X+1) :
                if d_map[k][x] <= Y and x + a <= X:#Nodeを発見したら実行する。
                    d_map[k+1][x+a] = min(d_map[k+1][x+a], d_map[k][x]+b)
        #print("##################################################")
    
    #これによりmapが作成された。中にはしょっぱみの価値がある。
    for k in range(N, -1, -1) :
        for x in range(X+1) :
            if d_map[k][x] <= Y :#初めて該当箇所を検知するまで実行
                print(min(k+1, N))
                return
    print(1)
    return

def forcheck2() :
    for i in range(1, -1, -1) :
        print(i)
    

if __name__ == "__main__" :
    main()
    #cheaker()
    #forcheck2()