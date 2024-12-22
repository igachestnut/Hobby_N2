""" 

発想
----
- 計算量
    - 各Node分だけ実行する。N
    - Nが重なる可能性がある最大数は、右上の左下の2点で考えたとき10000程度(N**2)
    - 以上より、全数調査で移動する。 

- らせん移動→移動する法則性は決まっている。
    右移動、上、左、下の順番⋀、2回ずつ同じ距離。
    →これは、方向と、回数が分かると、次進む位置が分かる。

- 複数の小人が同じ枡に移動する可能性だが、
    進む方向が全員で統一されているため、この事象は発生しない。
    
- 特殊ケースで間違いだった。
    - メモするMapの大きさを250として設定していたのが、
        四隅を起点とするMapをする際だと、足りない。
    - Mapサイズについての考察。
        入力値のx,yの最大最小の差で大きいほうの2倍と少しだけあると、最小限のMapで実装できそう。
        
"""

def cheaker() :
    direction_iterator = get_direction()
    for i in range(10): 
        print(next(direction_iterator))
    return

def main() :
    N = int(input())
    Nodes = []
    for i in range(N) :
        x, y = map(int, input().split())
        Nodes.append([x, y])
    
    #Mapの作成   
    #min_x, max_x = min(node[0] for node in Nodes), max(node[0] for node in Nodes)
    #min_y, max_y = min(node[1] for node in Nodes), max(node[1] for node in Nodes)
    #print(min_x, min_y)
    #print(max_x, max_y)
    #max_range = max(abs(max_x-min_x), abs(max_y-min_y))
    Map = [[False for i in range(404)] for j in range(404)]
    for n in Nodes :
        Map[n[1]][n[0]] = True #到達地点として記載。
    
    #移動処理の開始。
    result = 0
    queue = Nodes
    direction_iterator = get_direction()
    while queue :
        new_queue = []
        #print("出力中です")
        next_position = next(direction_iterator) #移動先位置を定義
        for que in queue :
            nx, ny = que[0]+next_position[0], que[1]+next_position[1] #次の位置
            if Map[ny][nx] : #移動可能かチェック
                continue #その点は終了する。
            Map[ny][nx] = True
            new_queue.append([nx, ny])
        
        result += 1
        queue = new_queue
    
    #print(Map)
    print(result-1)#もし移動可能なqueueが存在しない場合、余分にresultを追加していることになるため。
    return


def get_direction() :
    """ 次に進むべき方向を取得する関数 
    Returns
    --------
    [x, y] : int,int
        次に進むべき方向
    """
    num = 1
    
    while True :
        #右方向
        for i in range(num) :
            yield [1, 0]
            
        #上方向
        for i in range(num) :
            yield [0, -1]
        
        num += 1
        
        #左方向
        for i in range(num) :
            yield [-1, 0]
            
        #下方向
        for i in range(num) :
            yield [0, 1]
        
        num += 1



if __name__ == "__main__" :
    main()
    #cheaker()
