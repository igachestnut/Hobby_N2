""" 
発想

基本的な全数調査
Aiが食べる寿司をMだけ調べ、初めて条件合致したところを食べさせれば良い。
しかし、これだとN*Mだけかかってしまう。

探索時間を
log(M)にする方法
heapq()
10以上で、最も値の小さいM を調査する。

配列Ｂの優先度を再定義する。
- 10 j=1, 10 j=5だった場合、j=1のほうが早く抜き出ししたい。
- j の桁数をJとするなら、Mj+j/Jだけのfloat構造にすると優先度がつきそう。



...解釈を間違っていた。
人iが食べるものは、すべてのi以下である。



"""

def check() :
    return

import bisect
def main() :
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    J = len(str(M))+1
    new_B = [b+j/(10**J) for j,b in enumerate(B)]
    new_B.sort()
    result = [-1 for j in range(M)]
    for i,a in enumerate(A) :
        r = bisect.bisect(new_B, a)
        print(new_B)
        if r<len(new_B) :
            rp = new_B.pop(r) #もしかしたら計算量やばいかも
            print(rp)
            print((rp-float(int(rp)))*10**J)
            result[int((rp-float(int(rp)))*10**J)] = i+1
        #print(r)
    for r in result:
        print(r)
    return

import bisect
from collections import defaultdict
def main2() :
    """ defaltdictで数を制御する """
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    new_B = defaultdict(list)
    B_values = set()
    for j,b in enumerate(B) :
        new_B[b].append(j+1)
        B_values.add(b)
    B_values = sorted(B_values)
    B_values_list = list(B_values)
    
    # 人Aiが食べるであろうものを1つずつ定義していく。
    result = [-1 for j in range(M)]
    for i,a in enumerate(A) :
        if B_values == set() :
            break
        # 食べるでBjの値を取得→keyで調査して、該当するjを取得する。
        ri = bisect.bisect_left(B_values_list, a)
        if ri>=len(B_values) :
            continue
        rv = B_values_list[ri]
        j = new_B[rv].pop(0)
        result[j-1] = i+1
        if new_B[rv] == [] :
            B_values.remove(rv)
            B_values_list.pop(ri)
        #print(B_values)
    for r in result:
        print(r)
    return


from collections import defaultdict
def main3() :
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    new_B = defaultdict(list)
    B_values = set()
    for j,b in enumerate(B) :
        new_B[b].append(j+1)
        B_values.add(b)
    B_values = sorted(B_values)

    # 人Aiが食べるであろうものを1つずつ定義していく。
    result = [-1 for j in range(M)]
    for i,a in enumerate(A) :
        while B_values and B_values[-1]>=a :
            rv = B_values[-1]
            for j in new_B[rv]: result[j-1] = i+1
            B_values.remove(rv)
            
    for r in result:
        print(r)

import heapq
def main4() :
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    new_B = [[-b,j] for j,b in enumerate(B)]
    heapq.heapify(new_B)

    # 人Aiが食べるであろうものを1つずつ定義していく。
    result = [-1 for j in range(M)]
    for i,a in enumerate(A) :
        while new_B :
            tmp_b = heapq.heappop(new_B)
            if a>-tmp_b[0]: 
                heapq.heappush(new_B, tmp_b)
                break
            result[tmp_b[1]] = i+1
            
    for r in result:
        print(r)
    return


if __name__ == "__main__" :
    main4()
    #check()
