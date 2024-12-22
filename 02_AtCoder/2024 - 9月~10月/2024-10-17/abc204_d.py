""" 発想

Tiを2つに分配する
その差が最小になるときが答え。

選ぶか否かということで、
ナップサック問題に近いかも。
Ti<=10**3。
2**Nだけ通りが存在しそう。
全数は間に合わないだろうな。

N*Ti <10**5 であることを用いると,,?
とりあえずansはこう

dpT = N*Tiだけ
逆からdpで

queryはsetで追加する。



"""

def checker() :
    return

import bisect
def main() :
    """ 2つのオーブンを用いて、最短で料理をする速度を導出する問題 
    
    間違いでした。
    半分より大きい到達可能位置だと、挿入位置になってしまうため間違い。到達可能位置そのものを用いて答えを出すべき
    """
    N = int(input())
    T = list(map(int, input().split()))

    query = set()
    #dp = [1]+[0 for i in range(N*10**3)]
    sumT = sum(T)
    query.add(0)
    for i in range(N) :
        new_q = set()
        for q in query :
            #dp[q+T[i]] = 1
            new_q.add(q+T[i])
        query.update(new_q)
    print(query)
    
    reachable_locations = list(query)
    reachable_locations.sort()
    ans_i = bisect.bisect(reachable_locations, sumT//2)
    print(reachable_locations[ans_i])
    return

def main2() :
    """ 2つのオーブンを用いて、最短で料理をする速度を導出する問題 """
    N = int(input())
    T = list(map(int, input().split()))

    query = set()
    query.add(0)
    for i in range(N) :
        new_q = set()
        for q in query : new_q.add(q+T[i])
        query.update(new_q)
    print(query)
    
    reachable_locations = list(query)
    reachable_locations.sort()
    ans_i = bisect.bisect(reachable_locations, sum(T)//2)-1#半分以下の時間で、最大の時間位置を調査する。
    print(sum(T)-reachable_locations[ans_i])
    return


if __name__ == "__main__" :
    main2()
    #checker()
