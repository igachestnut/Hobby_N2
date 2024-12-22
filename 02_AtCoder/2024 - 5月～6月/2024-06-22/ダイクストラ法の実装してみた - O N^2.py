""" #####################################################
発想

[ダイクストラ法について-python](https://qiita.com/Yuya-Shimizu/items/eefdc6f854534e90c988)

## 条件
- 重みに負が存在しない
- ループが存在しない

## 実装イメージ
1. BFSっぽい実装
2. 最短経路を記録していく

## 計算量
Node数 = E, 辺数 = V とするならば、
O(V^2)       = O(N^2)    #ノーマルな実装 
### 自分の思う計算量
1. 確定していない重み群の中から最小だったindexを取り出す O(V)
2. その頂点vを確定。その頂点vから伸びる辺を調査(多くてE(全て1辺に集まっている場合)。だいたい1か2本でしょ!)
3. 結果が記入される。

## 流れ
1. 全ての頂点の結果を無限にする float('inf')
2. 始点の重み=0
3. 以下をループ
    1. 見えている範囲で一番重みが少ないのを抜き出す。(抜き出された情報は確定) 仮にmin_nodeとしよう
    2. min_nodeから全ての行き先とその重みをメモ (既に記入されていた場合→比較して、最小な方を適用)
    
## 自分なりにまとめてみる 結果的にはO(N^2)処理になった
0. node数= V, 辺数=E
1. result用リストの作成。[None for i in range(V)]
2. Nodeとedgeをまとめた情報を作成 (Eだけ作成)
    map = [[[1,2],[2, 3],[3, 3]], [], [], [[2, 10]]] (indexがNodeで、中の配列のindex0が行き先, 中の配列のindex1が重み)
3. queueの作成 {i : float("inf") for i in range(N)} → {"Node1" : "Value1", "Node2" :"Value2"}
4. 始点の設定 queue.[index] = 0
5. queueが無くなるまで実行 while queue : #一つづつ要素を抜き出すので 計算量O(V)
    1. queueの中から、一番小さいValueをもつNode情報を、NodeとValueで取り出す。
    min_node, min_value = None, float("inf")
    for node, value in queue.items() : #queの数だけ実行 O(V/2)=O(V)=O(N)だけ実行
        if min_node_value > min_value :
            min_node = node
    que = queue.pop(node) #que = {"Node" : "value"}の状態   
    2. 結果にメモ # 最小位置が確定→結果にメモする
    result[que.getkey()] = que.getvalue()
    
    3. 未確定距離情報達にメモ
    for edge, distance in map[que.getkey()] : #辺の数だけ実行
        queue[edge] = min(queue[edge], que.getValue() + distance) #min(もともとqueue内に入っていた距離と、開始地点の距離+移動するための距離）
    
## 自分なりにまとめてみる2 ヒープ(優先度付きqueue)を使用した場合？


##################################################### """
def cheaker() :
    return


def main() :
    return


if __name__ == "__main__" :
    main()
    #cheaker()
