""" #####################################################
発想

Aの位置を記憶するソート済みlist と、(dictでよさそう。)
全要素を格納するA を作成。

各配列には、前の要素の位置と次の要素の位置を[前の要素のあるAの位置, 後の要素のあるAの位置]
を格納するようにする。

- query 1
    - Aの末尾に要素を追加する。
    - Aの要素位置を格納したリストにアクセス。
    - 

Fail case
- 残りのリストが1個になるとき。
- 

- コツ
    - このリストは双方向リストと呼ばれるものである。
    - head, tail 頭とけつ を利用するといいかもね。
    - head, tail に直面する際は気を付けたい。


##################################################### """
def check() :
    a = [1]
    b = [1,2]
    print(" ".join(map(str, b)))
    print(" ".join(map(str, a)))
    print(*a)
    return

from collections import defaultdict
import sys

#sys.setrecursionlimit(5*10**5) #作成されるリストの最大回数だけ(もしかして再帰は深く潜り込む+帰ってくる？)
sys.setrecursionlimit(10**6)

def main() :
    N = int(input())
    A = list(map(int, input().split()))
    # リストAの要素aにO(1)でたどり着きたい。
    # key=A[i], value=[前の要素, 次の要素]を格納する便利dictを用いる
    neighbor_map = defaultdict(list)
    neighbor_map[A[0]] = [-1, -1]
    before_a = A[0]
    for a in A[1:] :
        neighbor_map[a] = [before_a, -1]
        neighbor_map[before_a][1] = a
        before_a = a

    # for key, value in neighbor_map.items() : print(key, value)

    # queryの実行
    Q = int(input())
    for q in range(Q) :
        query = list(map(int, input().split()))
        if query[0] == 1 : #query[1] =x(挿入した際の前の位置), query[2]=y(挿入したい数字)
            tmp_after = neighbor_map[query[1]][1] #次の位置を確認
            neighbor_map[query[2]] = [query[1], tmp_after] #与えられたqueryを用いて、新規dictの追加
            neighbor_map[query[1]][1] = query[2] #前の要素において、次の要素変更
            if tmp_after != -1 :
                neighbor_map[tmp_after][0] = query[2] #次の要素において、前の要素変更
        else : #Nodeの削除。map[x] = [-1, -1]になるとよい。
            [tmp_before, tmp_after] = neighbor_map[query[1]]
            if tmp_before != -1 :
                neighbor_map[tmp_before][1] = tmp_after #x直前のnodeにおいて、次の要素をxの次に変更
            if tmp_after != -1 :
                neighbor_map[tmp_after][0] = tmp_before #x直後のnodeにおいて、前の要素をxの前に変更
            neighbor_map[query[1]] = [-1, -1] #xは不要である。情報更新。(消してもいい、処理しなくてもよい)

    #for key, value in neighbor_map.items() : print(key, value)


    # 結果の出力 A[0]から最も頭の位置を参照する
    def get_head(mydict, x) :
        """ mydict(neigbor_map)の頭を調査する. 最悪計算量O(N)"""
        if mydict[x][0] == -1 : return x
        else : return get_head(mydict, mydict[x][0])
    
    # 配列の開始位置の特定
    x = 0
    for key, value in neighbor_map.items() :
        if value[0] == -1 :
            pass
        else :
            x = value[0]
            break 
    h = get_head(neighbor_map, x)

    result = [h]
    while neighbor_map[h][1] != -1 :
        h = neighbor_map[h][1]
        result.append(h)
    
    print(*result)
    return


def main2() :
    """ WA もしかしたら、neighbor_mapのlen(残った要素)が1つの時困惑している可能性がある。"""
    N = int(input())
    A = list(map(int, input().split()))
    # リストAの要素aにO(1)でたどり着きたい。
    # key=A[i], value=[前の要素, 次の要素]を格納する便利dictを用いる
    neighbor_map = defaultdict(list)
    neighbor_map[A[0]] = [-1, -1]
    before_a = A[0]
    for a in A[1:] :
        neighbor_map[a] = [before_a, -1]
        neighbor_map[before_a][1] = a
        before_a = a

    # for key, value in neighbor_map.items() : print(key, value)

    # queryの実行
    Q = int(input())
    for q in range(Q) :
        query = list(map(int, input().split()))
        if query[0] == 1 : #query[1] =x(挿入した際の前の位置), query[2]=y(挿入したい数字)
            tmp_after = neighbor_map[query[1]][1] #次の位置を確認
            neighbor_map[query[2]] = [query[1], tmp_after] #与えられたqueryを用いて、新規dictの追加
            neighbor_map[query[1]][1] = query[2] #前の要素において、次の要素変更
            if tmp_after != -1 :
                neighbor_map[tmp_after][0] = query[2] #次の要素において、前の要素変更
        else : #Nodeの削除。map[x] = [-1, -1]になるとよい。
            [tmp_before, tmp_after] = neighbor_map[query[1]]
            if tmp_before != -1 :
                neighbor_map[tmp_before][1] = tmp_after #x直前のnodeにおいて、次の要素をxの次に変更
            if tmp_after != -1 :
                neighbor_map[tmp_after][0] = tmp_before #x直後のnodeにおいて、前の要素をxの前に変更
            neighbor_map[query[1]] = [-1, -1] #xは不要である。情報更新。(消してもいい、処理しなくてもよい)

    #for key, value in neighbor_map.items() : print(key, value)

    # 配列の開始位置の特定
    h = 0
    for key, value in neighbor_map.items() : #つながりがあるNodeに到達するまで全調査。最大O(N+Q)なはず。(リストが最大量まで増えてもN+Q個だから)
        if value == [-1, -1]: continue
        else :
            h = key
            break 
    print(neighbor_map[h])
    while neighbor_map[h][0] != -1 :
        h = neighbor_map[h][0]

    result = [h]
    while neighbor_map[h][1] != -1 :
        h = neighbor_map[h][1]
        result.append(h)
    
    print(*result if len(result)>1 else result[0])
    return


def main3() :
    N = int(input())
    A = list(map(int, input().split()))
    # リストAの要素aにO(1)でたどり着きたい。
    # key=A[i], value=[前の要素, 次の要素]を格納する便利dictを用いる
    neighbor_map = defaultdict(list)
    neighbor_map[A[0]] = [-1, -1]
    before_a = A[0]
    for a in A[1:] :
        neighbor_map[a] = [before_a, -1]
        neighbor_map[before_a][1] = a
        before_a = a

    # for key, value in neighbor_map.items() : print(key, value)
    h = A[0] # 残った要素。必ず一つは存在するはず。

    # queryの実行
    Q = int(input())
    for q in range(Q) :
        query = list(map(int, input().split()))
        if query[0] == 1 : #query[1] =x(挿入した際の前の位置), query[2]=y(挿入したい数字)
            tmp_after = neighbor_map[query[1]][1] #次の位置を確認
            neighbor_map[query[2]] = [query[1], tmp_after] #与えられたqueryを用いて、新規dictの追加
            neighbor_map[query[1]][1] = query[2] #前の要素において、次の要素変更
            if tmp_after != -1 :
                neighbor_map[tmp_after][0] = query[2] #次の要素において、前の要素変更
        else : #Nodeの削除。map[x] = [-1, -1]になるとよい。
            [tmp_before, tmp_after] = neighbor_map[query[1]]
            if query[1] == h :#今回着目する要素(hedder代わり)を削除する場合
                h = max(tmp_after, tmp_before) #-1ではない要素をhedderとする。
            if tmp_before != -1 :
                neighbor_map[tmp_before][1] = tmp_after #x直前のnodeにおいて、次の要素をxの次に変更
            if tmp_after != -1 :
                neighbor_map[tmp_after][0] = tmp_before #x直後のnodeにおいて、前の要素をxの前に変更
            neighbor_map[query[1]] = [-1, -1] #xは不要である。情報更新。(消してもいい、処理しなくてもよい)

    #配列の最初の位置を特定する。
    while neighbor_map[h][0] != -1 :
        h = neighbor_map[h][0]

    result = [h]
    while neighbor_map[h][1] != -1 :
        h = neighbor_map[h][1]
        result.append(h)
    
    print(*result)
    return

if __name__ == "__main__" :
    main3()
    #check()
