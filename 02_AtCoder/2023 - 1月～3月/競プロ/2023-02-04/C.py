def cheaker() :
    return

def bfs(N) :
    #その頂点をチェックしたかどうかのメモ
    dist = [0 for _ in range(N+1)]#頂点とfor文のナンバーを併せます
    """
    考え方
    　distに頂点をメモって言って、
    もし、両方の値が1だった場合、count+=1する。
    この辺はいらないよと
    　しかし、この実装方法だと、つながっている島＋つながっている島であったばあい
    終わり両方ともTrueでやばいということ。
    """
def main2() :
    N,M = map(int,input().split())
    dist = [0 for _ in range(N+1)]
    ans = 0
    i = 0 #島
    
    #つながっているかどうかの確認
    for m in range(M) :
        a,b = map(int,input().split())
        if dist[a] == 0 and dist[b] == 0 :
            i += 1
        if dist[a] == dist[b] :
            ans += 1
        dist[a],dist[b] = i,i
        
    print(ans)
    return


from collections import deque

def DFS(dist,que,need,G) :
    #もしそこがたどり着いたことが無かった場合
    if dist[que] == False :
        print(dist)
        dist[que] = True
        print(dist)
        need += 1
        queue = deque(G[que])
        for k in range(len(queue)) :
            que = queue.popleft()
            print(que)
            dist,need = DFS(dist,que,need,G)
            print(que,"調べたqueはTrueでした")
    #もし既にたどり着いたことがある場合
    else :
        pass
    return dist,need
    
def main() :
    N,M = map(int,input().split())
    dist = [False for _ in range(N+1)]
    G = [set() for _ in range(N+1)]
    for i in range(M) :
        a,b = map(int,input().split())
        G[a].add(b)
        G[b].add(a)

    need = 0
    for i in range(len(G)) :
        #一番最初の始点を見つける作業
        if G[i] == [] :
            continue
        if dist[i] == False :
            dist[i] = True
            queue = deque(G[i])
            for k in range(len(queue)) :
                que = queue.popleft()
                dist,need = DFS(dist,que,need,G)
        #一度いったことがある場合、pass
        else :
            pass
    print(M - need)
    

if __name__ == "__main__" :
    main()
    #cheaker()

def MEMO() :
    """
    なぜか知らんけどREになってしまった。
    Mが増えた場合？に起こる感じ。
    それからうんともすんともいかずに撃沈した。
    メモリを使用しすぎる場合があるのかな？
    
    
    """
