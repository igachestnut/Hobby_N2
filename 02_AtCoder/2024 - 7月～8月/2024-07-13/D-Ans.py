""" #####################################################
発想

ダイクストラ法を使用する。

頂点に重みがあるため計算できない
→そこで、頂点u→vにおいて辺の重みをAだけ追加して、逆も同様に適用することで、
有効グラフとして扱うことができる。


##################################################### """


def cheaker() :
    return


def main() :
    """ グラフアルゴリズム　見えている辺orうえぃとの中で、一番軽いものを更新し続ける手法 """
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #行き先とWeightをまとめたリストを作成。
    #[[[3,2], [2,2]]] 第1Index＝現在の島 第二Index =その島から見えている辺の数 第三Index=[0]→見えている島、第三index=[1] = wight
    hen_map = [[] for n in range(N)]
    for i in range(M) :
        u, v, b = map(int, input().split())
        hen_map[u-1].append([v-1, b+A[v-1]])
        hen_map(v-1).append([u-1, b+A[u-1]])
    
    result_weight = [float("inf") for i in range(N)]
    result_weight[0] = 0
    is_search = [False for i in range(N)]
    is_search[0] = True
    queue = hen_map[0]

    while True :
        min_wight = float("inf") #現時点で見えている最低の値 
        min_index = 0 #現地点でいける最低のindexを知る。
        for que in queue :
            #MEMO - que[0]→見える頂点 que[1]→見える頂点に到達するまでの距離
            if is_search[que[0]] :#既に調査済みは実施しない。
                continue
            
            #ある程度最短重みを更新しつつ、次調査するべき点を導出したい。できればlog(n)で

            #値に更新があるかチェック。
            if que[1] < result_weight[que[0]] :
                #値に更新がある場合、
                result_weight[que[0]] = next_weight
            if result_weight[que[0]] < min_wight : #次の開始位置を記載する。
                min_wight = next_weight
                min_index = que[0] 
                
        queue = hen_map[min_index]
    
    
    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
