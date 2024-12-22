""" 発想

BFS
1から見えるすべての経路を幅優先探索で実施する。
1に最短でたどり着くものを見つけたら終了...?
計算量NM
"""

def check() :
    return

from collections import defaultdict
def main() :
    """ BFSで最短距離調査の実装。BFSで重みもないので値を更新する必要なし """
    N, M = map(int, input().split())
    node = [[] for i in range(N)] #node[i]において、次の位置を検査する
    dis = [float("inf") for i in range(N)] #そのNodeにおける、1からの最短距離
    for m in range(M) :
        a,b = map(int, input().split())
        node[a-1].append(b-1)
    
    queue = [0] #調査をし始めたいと思っている頂点を格納する
    now_dis = 1 #現在の1からの距離
    while queue :
        new_queue = [] #次のBFS調査位置
        for que in queue :
            for b in node[que] :#その頂点における全調査点を取得
                if dis[b] == float("inf") :
                    new_queue.append(b)
                    dis[b] = now_dis

        if dis[0] != float("inf") :
            print(dis[0])
            return
        now_dis += 1
        queue = [nq for nq in new_queue]

    else :
        print(-1)
    return


if __name__ == "__main__" :
    main()
    #check()
