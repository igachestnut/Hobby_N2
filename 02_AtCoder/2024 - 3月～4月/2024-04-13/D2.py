""" #################################################
D2.py

D.pyで間違ってしまった。
リストの作成と分けて実装する。

16:06

考え方
(1) 入力L~R において、経路として考えられる(Node)の全列挙をする
    



################################################ """
def cheaker() :
    return


def main() :
    L, R = map(int,input().split())
    
    #node(L~R)におけるすべてのつながりの取得
    connections = create_node_connections(L, R)
    
    #隣接リストの作成
    adjacent_node = create_adjacency_list(connections)
    
    #最短経路の探索
    keiro = BFS(L, R, adjacent_node)
    
    
    return

def create_node_connections(start, end) :
    """ 問題の条件において、start~end間のすべてのつながりを出力する関数 
    
    flow 
    -----------
    (1) start~endまで一つづつ実行
        (1) その点におけるすべての可能なi,jコンビを列挙
        (2) 末尾に追加
    """
    connections = []
    for n in range(start, end) : #n →Nodeの意
        #i,jのコンビネーションを全列挙
        combination_ij = []
        i = 0
        while 2**i < end :
            j = start/(2**i)
            combination_ij.append([i, j])
            i += 1
        
        #作成したijから到達できると思われる全てのlrを作成
        for [i, j] in combination_ij :
            l = n # 2**i*jと同義
            r = 2**i*(j+1)
            connections.append([l, r])
            
    return connections


def create_adjacency_list(connections) :
    """ nodeのつながりを記載したリストから、隣接リストを作成する。(型はset) """
    adjacent_node = {}
    for i in range(len(connections)) :
        [l,r] = connections[i]
        if l not in adjacent_node :
            adjacent_node[l] = set(r)
        else :
            adjacent_node[l].add(r)
        #有向グラフであるため、[r].add(l)はいらない
            
    
    #print(adhacent_node)
    return adjacent_node

def BFS(start, end, adjacent_node) :
    """ 幅優先探索. Goleまでの最短経路を探索する。 """
    distance = {key: None for key in adjacent_node} #隣接リストと同じ場所でNoneを記載したリストの作成
    
    #初期化
    dis = 1                      #最初の距離
    distance[start] = dis        #start位置の記載
    queue = adjacent_node[start] #start位置から見えるnodeの取得
    
    while queue :
        dis += 1       #階層を深める
        new_queue = [] #次階層の探索場所を保持する場所
        for que in queue :
            if distance[que] > 0 :
                continue
            else :
                pass
            distance[que] = dis                  #その地点における最短到達距離を記載
            new_queue.append(adjacent_node[que]) #記載

        queue = new_queue
        

    """ これによってその地点における最短を記載することはできたものの、
    経路が分からない。
    もしかしたら、disで代入するものを
    """



if __name__ == "__main__" :
    main()
    #cheaker()