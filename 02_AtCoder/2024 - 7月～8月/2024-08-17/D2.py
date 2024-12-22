""" 
発想
原点Node1から、全ての点に対するModを算出し、その数をメモ。

1. 各Nodeへの距離をModとして記録する。O(N)
    mod_map = [0 for m in range(M)]
2. その地点での行ける数というのが、Node(i)→Node(i+1)の距離(tmp_dis)と、
    mod_map の距離加算した際の値が0になる、
    すなわち、到達可能点は、mod_map[M-(Node(i)→Node(i+1))%M]である。
    Node1を考える際は、tmp_dis=0として考えれば、答えを出せる。
    O(N)

    ただし、sum(A)がmodM==0の場合、余分に計算することになるため、
    -1しなければならない。

従って、O(N +N)より十分高速に算出できそう

...ううぅぅんみすっぽい？
1周のみ換算だと、1-9は計算できても、9-3等が計算されていないことになってしまう為。
解説では、時計回りであることを利用して、移動領域を0~2N-1まで定義して計算しようとしていた。

1  2  3  4  1  2  3  4
+--+--+--+--+--+--+--+



"""

def cheaker() :
    return


def main() :
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    mod_map = [0 for i in range(M)]
    
    #1からの全距離(Mod)を計算し、その数をmod_mapに代入する。
    tmp_dis = 0
    for i in range(N) :
        tmp_dis += A[i]
        mod_map[tmp_dis%M] += 1
    
    #算出
    result = mod_map[0] -1
    for i in range(1, N) :
        #ずれの定義
        tmp_dis = A[i-1]
        result += mod_map[M-]
    return


if __name__ == "__main__" :
    main()
    #cheaker()
