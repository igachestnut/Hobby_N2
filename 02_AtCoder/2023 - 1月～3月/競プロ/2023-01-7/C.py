def BFS(v,Land_num,dist) :
    dist[v] = Land_num
    queue = G[v]
    while queue :
        que = queue.pop(0)
        if que == -1 :
            continue
        if dist[que] == -1 :
            dist[que] = Land_num
            for j in G[que]:
                queue.append(j)
        else :
            continue
    return dist


def bfs() :
    #初期設定
    dist = [-1 for _ in range(N)]
    dist_cheak_num = 0 #distで、-1の要素を見つけるよう。
    Land_num = 1#つながりの島の情報
    
    #dist内の要素を全て埋める作業（動的計画法？）
    for v in range(N) :#dist全探索
        if dist[v] == -1 :
            dist = BFS(v,Land_num,dist)
            Land_num += 1
        else :
            continue

    return max(dist)



N,M = map(int,input().split())
#各頂点ごとにつながりのある値を出力
G = [[-1] for _ in range(N)]
#ー１が値がないということなので、気を付けなければならない。。
for m in range(M) :
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
    
ans = bfs()
print(ans)

"""
入力
5 3
1 2
1 3
4 5
"""
