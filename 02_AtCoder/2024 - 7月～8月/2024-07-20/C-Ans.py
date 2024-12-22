""" 
tree = [[[]]]
- 第一index Level = 文字の決定数を示す。
- 第二index 行き先 = 文字を決定した場合、行き先の種類数を示す。 node
- 第三index 0 = 文字自体、index1=現地点での

queueの考え方と、Treeの構造を組み合わせたデータ列。
treeに追加するデータは、見なければならない情報として載せておくことで、無くなるまで実行の流れができる。
(流れに乗りながら順次作成削除が出来そう)

1. Nodeとqueue_Edgeの入力
2. 完遂かどうかチェック
    (1). 完遂→queueの取り出し、検査, 全てのqueueが無くなるまで実行。
        その後、queueの[]を取り除いて、上階へ結果を返す。
    (2). まだ→3.へ移動
3. 新Node作成と、作成元にしたEdgeを削除する。


MEMO
------------
- 一生クラス内のEdgeが新規作成しているはずなのに、元の変数の情報も書き変わってしまう現象が生じる
どうしよう。まじで
[参考資料-参照渡し](https://beginner-engineers.com/pass_by_reference/)
- 今までこの事象をが発生しなかった理由が分かった。
    1. クラス内で、同じリストを用いた参照を行ったことが無いこと。
        →今回のデータ構造は、木構造。
        Indexの他に、リスト情報も渡すようになる。
    だから面倒なことが起きている。
    これはこの先も多く発生する可能性が高い。→非常に厄介。
- 逆に今まで回避できていた理由が分かった。
    1. 今まではstrやintなど一つの情報ずつしかやり取りを行わなかったから。
"""
from typing import Union

class myNode :
    """ 現在の頂点における、見えている点と現時点のstring情報をまとめたクラス
    
    MEMO
    ---------
    - 次のmyNode情報をまとめたクラスを作成できる。
    """
    def __init__(self, now_string:str, edge) :
        self._Node_string = now_string #例)"", "a", "aa"
        self._Edges = edge             #例)[["a", 1],["b", 1]]
    
    def create_next_level_by_filaly_Node(self) :
        """ 現在のNode状況から、次へのNode情報をまとめたlevelを作成する関数 """
        def create_next_node(dif_index:int, node_string:str, edges:list) :
            if edges[dif_index][1] == 1 :#現在追加して終了する場合
                edges[dif_index].pop()
            else :
                edges[dif_index][1] -= 1
            return myNode(node_string, edges)
            
        next_level = []
        for i in range(len(self.Edges)) : #エッジの種類だけ、新edgeの作成
            new_myNode = create_next_node(
                dif_index=i,
                node_string=self.Node_string + self.Edges[i][0],
                edges=self.Edges
            )
            #new_myNode.get_states()
            next_level.append(new_myNode)
            
        print(f"作成した新規レベル{next_level}")
        return next_level
    
    def create_next_level_by_finally_Node(self) :
        """ 現在のNode状況から、次へのNode情報をまとめたlevelを作成する関数 """            
        next_level = []
        for i in range(len(self.Edges)) : #エッジの種類だけ、新edgeの作成
            new_node_string = self.Node_string + self.Edges[i][0]
            new_edges = [[s, e] for s, e in self.Edges]
            #print(f"new_edges")
            #print(new_edges)
            if self.Edges[i][1] == 1 :
                new_edges.pop(i)
                #print(f"popされました{new_edges}")
            else :
                new_edges[i][1] -= 1
                #print(f"elementが引かれました{new_edges}")
            new_myNode = myNode(new_node_string, new_edges)
            #new_myNode.get_states()
            next_level.append(new_myNode)
            
        #print(f"作成した新規レベル{next_level}")
        return next_level
    
    def get_states(self) :
        return f"Node_string:{self.Node_string}, Edge:{self.Edges}"
    
    @property
    def Edges(self) :
        return self._Edges
    @property
    def Node_string(self) :
        return self._Node_string
            
def main2() :
    N, K = map(int, input().split())
    S = list(input())
    
    #初期位置から見える、行き先(Edge_list)の作成
    set_S = set(S)
    Edge_list = [[str(s), 0] for s in set_S]
    for s in S :
        for e in Edge_list :
            if s == e[0] :
                e[1] += 1
                break
    print(Edge_list)
    
    #treeの作成
    my_first_node = myNode("", Edge_list)
    Level1 = [my_first_node]
    tree = [Level1]

    
    def not_palindrome_count(s:str) -> int :
        """ 入力された文字列に対して、回文ではなかった数を返す関数 """
        for i in range(0, len(s)-K+1) :        
            for j in range(K//2) :
                if s[i+j] == s[i+K-1-j] :#回文ではない判定
                    #print(f"文字列{s}において、回文判定出ました。")
                    return 0
        return 1
    
    def tree_search(count) -> int :
        """ 再帰関数。Treeの中身が無くなるまで実行する。
        
        Flow
        -----
        1. TreeObjにおける、最終レベルの状態確認。
            1. 最終レベルにおいて、Nodeが存在しない。→不要なオブジェクトを削除して(levelを削除して)上階に戻る。
            2. 最終レベルにおいて、Nodeが存在し、文字列も完成されている→カウントし、(levelを削除して)上階へ戻る。
            3. 最終レベルにおいて、Nodeが存在するが、不完全でまだ深く探索できる。→新規にNewLevelを作成、実行

        """
        #最終レベルにオブジェクトが存在しているのか確認
        while tree[-1] != [] :#最終levelに何も格納されていない状態になるまで実行する。
            #最終レベルにオブジェクトが存在し、文字列も完成状態
            #print(tree[-1][0].Node_string , "node-----string")
            if len(tree[-1][0].Node_string) == N or tree[-1][0].Edges == []:#これ以上深く潜れない場合。最大レベルの全文字列におけるカウントを実行、削除して上階へ戻る。
                now_level = tree.pop()
                for node in now_level :
                    #print(node.get_states())
                    count += not_palindrome_count(node.Node_string)
                continue
            
            #もしNodeが存在するが、不完全でまだ深く探索できる 
            # 一番後ろのNodeを吹き出す→nextlevelの作成
            tmp_node = tree[-1].pop()
            #print(f"階下を作成します。使用するnode_str:{tmp_node.Node_string}, edge:{tmp_node.Edges}")
            next_level = tmp_node.create_next_level_by_finally_Node() 
            tree.append(next_level)
            #print("下階へご案内ー")
            count = tree_search(count)
            #print("////////////")
            print(tree)
    
        tree.pop()
        print("上階へ移動しまーす")
        return count
        
        
    #探索の開始
    result = tree_search(0)
    print(result)
    return
        

if __name__ == "__main__" :
    main2()
    #cheaker()
