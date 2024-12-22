""" アルゴリズムの設計コンセプト

木構造で文字列作成。
Point
- 木構造であるため、各レベルにおいて、作成可能な文字列しか追加しない。
    →全列挙より、かぶりが生じるほど効率的に列挙できる。
    オーダーO(N!)である。だが、文字列同士でかぶりLが生じると、O((N-L)*((N-1)-(L-1)*,,,)のようになる？
    ※自分で考えた割には、あまり効率的ではないかもしれない。
- 深さ優先探索風に作成することで、作成に必要なNode情報を最低限に抑え、
    メモリを節約しながら作成できる

高速化するために更なるアイデア
- Node_Sをlenで回すと、0の際に時間を食うことになりそう。→必要な探索回数をqueとして保持すると効率が上がりそう。


その他MEMO
- python 参照渡しと値渡し。
    どうやらlistを再帰関数内で渡しあう時は、.copyを使用しないと、参照私になってしまうようである。
    

"""

import time
def cheaker() :
    v = 8
    t1 = time.time()
    L1 = [i for i in range(10**v)]
    print(time.time()-t1)
    t2 = time.time()
    L2 = []
    for i in range(10**v) :
        L2.append(i)
    print(time.time()-t2)
    t3 = time.time()
    L3 = list(range(10**v))
    print(time.time()-t3)
    return


def main() :
    N, K = map(int, input().split())
    S = list(input())
    
    #Nodeの作成
    set_S = set(S)
    node_S = [[s, 0] for s in set_S]
    for i, ss in enumerate(set_S) : #存在する文字列だけ着目
        newS = []
        for s in S : #全ての文字列だけ実施。
            if s == ss :
                node_S[i][1] += 1
            else :
                newS.append(s)
        S = newS
            
    #print(node_S)
    s = ""
    result = union_map(s, node_S, K, 0)
    print(result)
    return

def union_map(s:str, node_S:list, K:int, result:int):
    """ 木構造で文字列をかぶりなしで作成し、出力を行うアルゴリズム。
    
    parameters
    --------------
    - s : string 
        現時点で作成済みのString
    - node_S : list[[int,int]] 
        その地点において、次に見えそうな地点。
    - K : stringの長さ。到達地点
    - result :int
        カウント数
    """
    print("----")
    print(s)
    print(node_S)

    #入力された文字列は、完成されているのか確認
    if not node_S :
        #回文の調査
        count = 0
        for i in range(0, len(s)-K+1) :        
            for j in range(K//2) :
                if s[i+j] != s[i+K-1-j] :#回文ではない判定
                    count += 1
                    print(f"s:{s}, sのチェック{s[i:i+K-1+1]}")
                    break
        print(f"今回検査した結果、回文無し文字列は{result+count}だけ存在しました。")
        return result + count
  
    #作成足りないなら、次のNode情報を作成して、存在する分だけ再帰処理  
    print(f"新しく追加nodeを作成します。lenは{len(node_S)}です。")
    for n in range(len(node_S)) :
        copy_node = node_S.copy() #new_node[次に追加したい番号][0=文字列, 1=残り追加数]
        new_s = s + str(copy_node[n][0]) #新規文字列の作成   
        #Nodeの残り追加数を確認する
        if copy_node[n][1] == 1 : #着目しているNodeにおいて、追加できる残り数が1でラストなら
            copy_node.pop(n)
            new_node = copy_node.copy()
            result = union_map(new_s, new_node, K, result) #着目しているque番号のnodeにおいて、該当する文字列を削除する。
        else :
            copy_node[n][1] -= 1
            new_node = copy_node.copy()
            result = union_map(new_s, new_node, K, result) #着目しているque番号のnodeにおいて、element数を1少なくする。
        
    return result
        
""" ここで新発想

変数 treeを定義して考えることとする。
BFSの途中に、一回一回見えている範囲を定義することをしていると、非効率であることが分かった。
そこで、予めTreeのレベル(深度)を定義して考えよう！という方向性。
今回Treeは、文字数Nに依存することになりそう。

というか、ここで言うTreeのNodeとして入れるべき情報は、
見えている辺よりも、
s 自体ではないだろうか？

もしくは、

tree = [[[]]]
- 第一index Level = 文字の決定数を示す。
- 第二index 行き先 = 文字を決定した場合、行き先の種類数を示す。 node
- 第三index 0 = 文字自体、index1=現地点での
例)
N=3, K=3
aabの場合

[
    #Level数
    [
        #Nodeの状態と、見えている行き先例
        {
            "Node-String" : None,
            "Edge" : [
                ["a", 2],
                ["b", 1]
            ],
        }
    ],
    [
        {
            "Node-String" : "a",
            "Edge" : [
                ["a", 1],
                ["b", 1]
        },
        {
            "Node-String" : "b",
            "Edge" : [
                ["a", 2]
            ]   
        }
    ],
    ...
]

[[{"Node-String" : None,"Edge" : [["a", 2],["b", 1]],}],
 [{"Node-String" : "a","Edge" : [["a", 1],["b", 1]},
  {"Node-String" : "b","Edge" : [["a", 2]]}
 ],...]


queueの考え方と、Treeの構造を組み合わせたデータ列。
treeに追加するデータは、見なければならない情報として載せておくことで、無くなるまで実行の流れができる。
(流れに乗りながら順次作成削除が出来そう)

1. Nodeとqueue_Edgeの入力
2. 完遂かどうかチェック
    (1). 完遂→queueの取り出し、検査, 全てのqueueが無くなるまで実行。
        その後、queueの[]を取り除いて、上階へ結果を返す。
    (2). まだ→3.へ移動
3. 新Node作成と、作成元にしたEdgeを削除する。
"""
class myNode :
    """ 現在の頂点における、見えている点と現時点のstring情報をまとめたクラス
    
    MEMO
    ---------
    - 次のmyNode情報をまとめたクラスを作成できる。
    """
    def __init__(self, now_string:str, edge:list[str, int]) :
        self.Node_string = now_string #例) None, "a", "aa"
        self.Edges = edge #例)[["a", 1],["b", 1]]
    
    def create_next_level_by_filaly_Node(self) :
        """ 現在のNode状況から、次へのNode情報をまとめたlevelを作成する関数 """
        next_level = []
        for i, edge in enumerate(self.Edges) :
            new_string = self.Node_string + edge[0]
            #新edgeの作成
            if edge[1] == 1 :#現在追加して終了する場合
                new_edge = self.Edges
                new_edge.pop(i)
            else :
                new_edge = self.Edges
                new_edge[i][1] -= 1
             
            new_myNode = myNode(new_string, new_edge)
            next_level.append(new_myNode)
        return next_level            
            
def main2() :
    N, K = map(int, input().split())
    S = list(input())
    
    #初期位置から見える、行き先(Edge_list)の作成
    set_S = set(S)
    Edge_list = [[s, 0] for s in set_S]
    for s in S :
        for e in Edge_list :
            if s == e[0] :
                e[1] += 1
                break    
    
    #treeの作成
    my_first_node = myNode(None, Edge_list)
    Level1 = [my_first_node]
    tree = [Level1]

    
    def not_palindrome_count(s:str) -> int :
        """ 入力された文字列に対して、回文ではなかった数を返す関数 """
        count = 0
        for i in range(0, len(s)-K+1) :        
            for j in range(K//2) :
                if s[i+j] != s[i+K-1-j] :#回文ではない判定
                    count += 1
                    print(f"s:{s}, sのチェック{s[i:i+K-1+1]}")
                    break
        print(f"今回文字列{s}を検査した結果、回文無し文字列は{count}だけ存在しました。")
        return count
    
    def tree_search() -> int :
        #最大レベルは、結果となりうるStringが格納されているのか？
        if len(tree[-1][0]["Node-String"]) == K or tree[-1][0]["Edge"] == []:#これ以上深く潜れない場合。
            #treeの最大レベルが無くなるまで実行
            count = 0
            queue = tree.pop(-1)
            for que in queue :
                count += not_palindrome_count(que["Node-String"])
            return count

        #もう一つ深く潜れそうな場合。next_levelの作成
        if tree[-1] == [] :
            return count
        node_obj = tree[-1].pop(-1)
        next_level = node_obj.create_next_level_by_filaly_Node() 
        tree.append(next_level)
        result = tree_search()        
        return result
        
    #探索の開始
    result = tree_search()
    print(result)
    return
        

if __name__ == "__main__" :
    main()
    #cheaker()
