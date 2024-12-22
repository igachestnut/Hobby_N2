"""  
MEMO

山の面積を求める問題に帰着する。

1<= i < N で、A[i],A[i+1]において、
A[i] < A[i+1] →山が大きくなる。新規四角形を追加する
A[i] = A[i+1] →山が変わらない。pass
A[i] > A[i+1] →山が小さくなる。→定義されている四角形のうち、A[i+1]以上のxを持つ四角形をいくつか確定する。
それぞれの大きさを計算し,max値のみ残す。計算済みの四角形は削除する。
最後に、現在の大きさの高さxだけの四角形を新規作成する。..→？？？これをどうするの？やっぱり動的計画法っぽく解きたいけどまだわからん。

四角形の情報において、必要な情報は、
左の位置l, 高さx の二つがわかると、rの位置がわかるだけで面積を計算することができるようになる。

次の障壁
どうやってl,xの情報を保持しようか。
xの高さ重要。


xごとで、未確定な四角形の中で、最も左にある位置を格納するリストを作る?
ただ、これだとO(N*A)になってしまいそう。Aの閾値上下前部に値を格納することになりそうだから。
どうしよう。
越していて、最も最低の左上のいちがわ



"""

def cheaker() :
    return


def main() :
    N = int(input())
    A = list(map(int, input().split()))

    result = 0
    squere_p = [[0, 0], [A[0], 1]] #四角形の始点(左上の位置)を記したリスト。[x,l]という形式のリストが格納され、xの大きさ順となる。
    for i in range(1, N) :
        if A[i] > A[i-1] : squere_p.append([A[i], i+1])
        elif A[i] == A[i-1] : continue
        else : #山の高さが減少する場合。四角形を確定しつつ、最も大きな四角形を作る。
            while squere_p[-1][0] > A[i] : #現在のA[i]より左上に存在する点が存在するとき、四角形の面積を確定する。
                sp = squere_p.pop()
                #print(f"sp{sp}, i{i}, r{sp[0]*(i+1 -sp[1])}")
                result = max(result, sp[0]*(i+1 -sp[1])) #x * (r-l)の意
            squere_p.append([A[i], sp[1]]) #追加する四角形は、A[i]と同じ大きさで作成できる最も左に位置する山
    
    # 残りの山に残っている始点を用いて面積を計算する
    while squere_p :
        sp = squere_p.pop()
        result = max(result, sp[0]*(N+1-sp[1]))

    print(result)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
