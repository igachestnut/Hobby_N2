def cheaker() :
    return

def Random() :#実行時のエラーが分からなかったため
    import random
    import os
    TXT = "c-alg.txt"

    n , m = 20000 , 20000

    with open(TXT,mode="w",encoding="UTF-8") as f :
        f.write("{} {}\n".format(n,m))
        for i in range(m) :
            Line = [int(random.random()*n) , int(random.random()*n)]
            #print(Line)
            if Line[0] == Line[1] :
                Line = [1,2]
            Write_str = "{} {}\n".format(str(Line[0]),str(Line[1]))
            f.writelines(Write_str)
            
        

from collections import deque

def DFS(dist,que,need,G) :
    #もしそこがたどり着いたことが無かった場合
    if dist[que] == False :
        dist[que] = True
        need += 1
        queue = deque(G[que])
        for k in range(len(queue)) :
            que = queue.popleft()
            dist,need = DFS(dist,que,need,G)
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
    Random()
    #cheaker()

def memo() :
    """
    Error発見しました。
    RecursionError: maximum recursion depth exceeded in comparison

    Pythonが許容する 再帰処理の回数 を超えると
    プログラムが下記のようなエラーが出て停止するようになります

    デフォルトは1000回らしい。
    import sys
    sys.setrecursionlimit(2000)
    で最大再帰回数を2000回まで上げることができる。

    ...んまぁこうゆうERRORが出るならアルゴリズムの見直しをした方がいいけどね。

    次に学びたいこと
    　深さ優先探索で、こういったエラーを出さない方法について

    　⇒クラスで実行するUnionfind!
    　今までグラフは適当な物だったけど、ちょっと学んでみよう！
    """
