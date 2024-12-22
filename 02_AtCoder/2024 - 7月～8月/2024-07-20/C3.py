class myNode :
    """ 現在の頂点における、見えている点と現時点のstring情報をまとめたクラス
    
    MEMO
    ---------
    - 次のmyNode情報をまとめたクラスを作成できる。
    """
    def __init__(self, now_string:str, edge) :
        self._Node_string = now_string #例)"", "a", "aa"
        self._Edges = edge             #例)[["a", 1],["b", 1]]
    
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
    #print(Edge_list)
    
    #treeの作成
    my_first_node = myNode("", Edge_list)
    Level1 = [my_first_node]
    tree = [Level1]

    def is_palindrome_count(string:str) -> bool :
        """ 入力された文字列に対して、回文ではなかった数を返す関数 """
        #print(f"s{s}")
        for i in range(0, len(string)-K+1) :
            s = string[i:i+K] 
            if s == s[::-1] :
                return False
            #for j in range(K//2) :
            #    if s[i+j] == s[i+K-1-j] :#回文ではない判定
            #        if K//2 == j+1 :
            #            #print(f"文字列{s}において、回文判定出ました。")
            #            return False
            #    else :
            #        break
        return True
    
    def tree_search(count) -> int :
        """ 再帰関数。Treeの中身が無くなるまで実行する。
        
        Flow
        -----
        1. TreeObjにおける、最終レベルの状態確認。
            1. 最終レベルにおいて、Nodeが存在しない。→不要なオブジェクトを削除して(levelを削除して)上階に戻る。
            2. 最終レベルにおいて、Nodeが存在し、文字列も完成されている→カウントし、(levelを削除して)上階へ戻る。
            3. 最終レベルにおいて、Nodeが存在するが、不完全でまだ深く探索できる。→新規にNewLevelを作成、実行

        """
        #最終レベルにオブジェクトが存在している状態。
        for _ in range(len(tree[-1])) :
            if len(tree[-1][0].Node_string) == N :#これ以上深く潜れない場合。最大レベルの全文字列におけるカウントを実行、削除して上階へ戻る。
                now_level = tree.pop()
                for node in now_level :
                    if is_palindrome_count(node.Node_string) :
                        count +=1
                #print("上階へ移動しまーす")
                return count
            
            #もしNodeが存在するが、不完全でまだ深く探索できる 
            # 一番後ろのNodeを吹き出す→nextlevelの作成
            tmp_node = tree[-1].pop()
            #print(f"階下を作成します。使用するnode_str:{tmp_node.Node_string}, edge:{tmp_node.Edges}")
            next_level = tmp_node.create_next_level_by_finally_Node() 
            tree.append(next_level)
            #print("下階へご案内ー")
            count = tree_search(count)
            #print("////////////")
            #print(tree)
            
        #最終レベルにオブジェクトが存在しているのか確認
        if tree[-1] == [] :
            tree.pop()
            return count
        else :
            print("!?")
        
        
    #探索の開始
    result = tree_search(0)
    print(result)
    return
        

if __name__ == "__main__" :
    main2()
    #cheaker()
