def cheaker() :
    return


def main() :
    N, M = map(int, input().split())
    Map = create_map(N, M)
    dis_Map = create_distance_map(Map)
    
    for i in range(N) :
        print(dis_Map[i])
    return

def create_map(LEN, edge) :
    """ 入力の全a,bからつながっている場所を作成する関数
    
    MEMO
    --------
    (1) indexの番号
        全てfor文の0~N-1に合わせる
    """
    Map = [set() for l in range(LEN)]
    for e in range(edge) :
        a, b = map(int, input().split())
        Map[a-1].add(b-1)
        Map[b-1].add(a-1)
    
    return Map

def create_distance_map(Map, start=0) :
    """ 番号1の島から最短距離を記入したリストを返す関数 
    
    Parameters
    --------------
    Map : list(set())
        各島からのつながりを記載したリスト
    start : int
        開始位置
        ※for文で回すときは-1すること
        
    Return
    --------------
    dis_Map : list(int,,)
        各島において、startからの距離を記載したリスト
    """
    #距離mapの初期化。最短を見つけたいため、初期段階では極長の情報を入れておく
    Map_shape = len(Map)
    dis_Map = [-1 for _ in range(Map_shape)]
    
    queue = set([start]) #調査位置を記載するリスト
    dis   = 0            #調査位置からの距離
    
    #BFSの実行
    while queue : #調査位置が無くなるまで実行
        new_queue = set()
        
        # 今見えている全ての島を探索する
        for que in queue :
            # もし見えている島が新しい場合、
            # 再調査の必要があるため
            # 情報更新、queueの追加
            # (Noneではない既に発見した場所は、BFSの特性上最短になるため無視していい)
            if dis_Map[que] == -1 :
                dis_Map[que] = dis
                for item in Map[que] :
                    new_queue.add(item)
            
        dis += 1          #次の調査は距離が1増える
        queue = new_queue #次の調査場所の更新
        
    return dis_Map

if __name__ == "__main__" :
    main()
    #cheaker()
