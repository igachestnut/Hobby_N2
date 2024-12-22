""" #####################################################
発想

書き換える量の最小は?
- 条件
    - 2種類
    - 同じ数だけの文字

- 結果の文字列は2種類のみ
    - /\/\/\ or \/\/\/
    - それぞれ最小回数を求めようの会。

- 入れ替える回数はどうやって求めるのか?
    - 現在うまくいっていない文字列の数を列挙する。
    - (count //2) or N //2 -(count //2)が答え 

- 書き換える→ 2a_i, 2a_i+1,, のうち最もこたえが出てくる文字列が正解
    
MEMO
- defaltdict でmaxvalueを検査したとき、
vの値のmaxがどの数字かわからんケースが存在する。
maxvalueが2つある場合、どちらかにすればいいので問題ないが、
どうしたものか,,,
必要な情報
d1[i1] = --- (2a_i, 2a_i+1.. におけるmaxvalue)
d1[i2] = xxx (...            におけるmaxvalueの次の候補)
d2[i3] = mmm (2a_i +1, 2a_i+1 +1 におけるmaxvalue)
d2[i4] = mmm (2a_i +1, 2a_i+1 +1 におけるmaxvalueの次の候補)

if i1 == i2 :
    tmp_i = i2 if d1[i2] > d2[i4] else i4
    
##################################################### """
def check() :
    return

from collections import defaultdict
def main() :
    """ WA 
    
    どうしても、各配列における最大数と2番目の最大数の定義ができない。
    """
    n = int(input())
    v = list(map(int, input().split()))

    result = 0
    d1, d2 = defaultdict(int), defaultdict(int)
    for i in range(0, n-1, 2) : d1[v[i]] += 1
    for i in range(1, n, 2) : d2[v[i]] += 1
    print(d1)
    print(d2)
    print("-------------------------")
    i1, i2, i3, i4 = 0, 0, 0, 0 #i1,i2 = d1におけるmaxvalueの数字. i3,i4 =d2におけるmaxvalueの数字
    d1_count, d2_count = -1, -1
    for d1i, d2i in zip(d1.keys(), d2.keys()) :
        if d1[d1i] > d1_count :
            i2 = i1
            i1 = d1i
            d1_count = d1[d1i]
        if d2[d2i] > d2_count :
            i4 = i3
            i3 = d2i
            d2_count = d2[d2i]
    print(i1, i2, i3, i4)
    print(d1[i1], d1[i2], d2[i3], d2[i4])
    if i3 == i1 :
        if d1[i2] > d2[i4] :
            result = n - d1[i1] - d1[i2]
        else :
            result = n - d1[i1] - d2[i4]
    else :
        result = n- d1[i1] -d2[i3]

    print(result)
    return


from collections import defaultdict
import heapq
def main2() :
    """ 
    
    方向性の整理。
    1. まずどの文字を配列として採用するべきなのかを知りたい。
    2. その文字を採用したときの変数

    - 1.の深堀り
        - 2の倍数で出てくる数字と、2の倍数+1ででてくる数字は分けることができる。
        - 
    
    """
    n = int(input())
    v = list(map(int, input().split()))

    # 2の倍数, 2の倍数+1 にvを分類したとき、各値の要素数を調査する
    d1, d2 = defaultdict(int), defaultdict(int)
    for i in range(0, n-1, 2) : d1[v[i]] += 1
    for i in range(1, n, 2) : d2[v[i]] += 1

    # 各配列において、最大数と準最大数を定義する。(heapqに入力して、第一要素と第２要素を取得できるようにする)
    d1_deque, d2_deque = [], [] 
    for d1i in d1.keys(): d1_deque.append([-d1[d1i], d1i]) #[格納されている最大数, そのindex]
    for d2i in d2.keys(): d2_deque.append([-d2[d2i], d2i])
    heapq.heapify(d1_deque)
    heapq.heapify(d2_deque)

    # 値の決定をする
    d1_max_index = heapq.heappop(d1_deque)
    d2_max_index = heapq.heappop(d2_deque)
    if d1_max_index[1] != d2_max_index[1] : #最大の数値が違う場合。
        print(n +d1_max_index[0]+d2_max_index[0]) #n(最大数)-(変えなくていい量d1+d2)  ※heapqで反転させている
    else :
        d1_second_max_index = heapq.heappop(d1_deque) if len(d1_deque) > 0 else [0, -1] #[0, -1] 要素を変えられない(確定できない)ので0
        d2_second_max_index = heapq.heappop(d2_deque) if len(d2_deque) > 0 else [0, -1]
        if d1_max_index[0] == d2_max_index[0] :
            print(n + d1_max_index[0] + min(d1_second_max_index[0], d2_second_max_index[0]))
        elif -d1_max_index[0] > -d2_max_index[0] : #d1の方が最も多くの要素数なとき
            print(n + d1_max_index[0] + d2_second_max_index[0])
            #print(d1_max_index, d2_second_max_index)
        else :
            print(n + d2_max_index[0] + d1_second_max_index[0])
    return

if __name__ == "__main__" :
    main2()
    #check()
