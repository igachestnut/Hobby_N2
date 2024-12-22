""" 

roopすることはわかったので、
roopする最短の量を各Nodeで調査することで答えを算出しようとしたが、
2 3 4 1のようなテストケースは
3 4 1 2
1 2 3 4 のようにroopが関係なくなることが生じるため、わからんくなった。

また、もしきれいにroopしていたとしても、
Nのすべての要素を使用する場合、
従属の調査にはO(N)でいいが、
Pの調査には O(N *N?)がかかってしまうため、TLEとなりそう。
どうすればいいんだ
...


"""
def check() :
    return


def main() :
    """ 入れ替えられる番号は、roopする。
    
    この特性を生かす。
    各値のroop順番を記載していって、最初と同じになったら終了する。をすべてのqueue分

    roopの従属関係を調査して、roopを定義

    """
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    result = [-1 for i in range(N)]

    P_roop_nums = [-1 for i in range(N)] #現在のNodeは、何回処理すればroop処理になるか
    for i in range(N) :
        if result[i] != -1 : continue
        head_p = P[i]
        queue = set()
        queue.add(i+1)
        pi = P[i]
        while head_p != P[pi] :#roopの終わりにたどり着くまで実行
            queue.add[P[pi]]
            pi = P[i]

        roop_K = K % (len(queue) -1) if len(queue) > 1 else 1 #エスパー 仮のroop回数を用いて、処理回数を定義
        j = 1
        now_P = []
        while roop_K != j : 
            break

    
        




    return


if __name__ == "__main__" :
    main()
    #check()
