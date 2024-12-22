"""
a2 でTLEだった。

A[i1] < A[i2]を満たすi2に幅があるためである。

では、
中の要素はd[xx] xx以上の数値でもっとも左側に位置するindexを格納するものを作り出せば。。？
di = [0 ~ 10**9]

すると、入力i で、それ以上のindexで最低を教えてくれる。
ただ、配列を作り出すのに時間がかかりすぎるかも..?
checkpoint として、
逆から,,




"""
def checker() :
    return

from collections import defaultdict
def main() :
    """ 便利配列を用いた導出 
    
    Aの左側(score)に換算される部分をA1, Aの右側はA2としている。
    A1, A2の各要素一つを入れ替える(A1の要素i1をA2の1番目に、A2の要素i2をA1の-1番目に移動する)場合の処理回数がi2-i1である。これの全調査と、最小を調査する。
    A1のデータ構造を、dictで、調査したい数値をkey、調査したい数値があるindex番号をvalueとして格納する。
    """
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    A1, A2 = defaultdict(int), defaultdict(int) #最も左or最も右に位置する番号を格納するディクト ※注意: i2だけそれ以上で条件が合致している場合、その最小も適用可能ということで使用する。
    A1_set, A2_set = set(), set()
    for i1 in range(K) : 
        A1[A[i1]] = i1
        A1_set.add(A[i1])
    for i2 in range(N-1, K-1, -1) :
        A2[A[i2]] = i2
        A2_set.add(A[i2])

    A1_values, A2_values = list(A1_set), list(A2_set)
    A1_values.sort(), A2_values.sort() #各かぶりなしAi値を最小順番にする。

    # A2の更新。集合A2は、a:i の形式である。この際のa = 取りうるAの値, i=aをとるときの左の値。
    # ここから、i を a**以上**をとるときの左の値に更新する。
    tmp = A2[A2_values[-1]]
    for a2v in A2_values[::-1] :
        tmp = min(tmp, A2[a2v])
        A2[a2v] = tmp 

    # リスト内の数字で、最も小さい入れ替え回数の調査
    result = float("inf")
    i2 = 0
    for i in range(len(A1_values)) :
        while i2 < len(A2_values) :
            if A1_values[i] >= A2_values[i2]: #要素が領域内だが、入れ替え不可能な時
                i2 += 1
            else :
                break
        
        if i2 >= len(A2_values) : break #もう入れ替えられる数字A2が存在しない場合、調査の終了
        else :
            result = min(result, A2[A2_values[i2]]-A1[A1_values[i]])

    if result == float("inf") : print(-1)
    else : print(result)
    return


if __name__ == "__main__" :
    main()
    #checker()
