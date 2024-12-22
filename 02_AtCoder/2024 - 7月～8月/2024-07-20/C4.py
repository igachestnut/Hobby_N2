class myNode :
    def __init__(self, now_string:str, edge) :
        self.Node_string = now_string #例)"", "a", "aa"
        self.Edges = edge             #例)[["a", 1],["b", 1]]
    
    def create_next_level_by_finally_Node(self) :
        """ 現在のNode状況から、次へのNode情報をまとめたlevelを作成する関数 """            
        next_level = []
        for i in range(len(self.Edges)) : #エッジの種類だけ、新edgeの作成
            new_node_string = self.Node_string + self.Edges[i][0]
            new_edges = [[s, e] for s, e in self.Edges]
            if self.Edges[i][1] == 1 :
                new_edges.pop(i)
            else :
                new_edges[i][1] -= 1
            next_level.append(myNode(new_node_string, new_edges))
        return next_level
    
    def is_palindrome_count(self, K) -> bool :
        """ 入力された文字列に対して、回文ではなかった数を返す関数 """
        for i in range(0, len(self.Node_string)-K+1) :
            s = self.Node_string[i:i+K] 
            if s == s[::-1] :
                return False
        return True
                    
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
    #treeの作成
    my_first_node = myNode("", Edge_list)
    Level1 = [my_first_node]
    tree = [Level1]

    def tree_search(count) -> int :
        """ 再帰関数。Treeの中身が無くなるまで実行する。 """
        for _ in range(len(tree[-1])) :
            if len(tree[-1][0].Node_string) == N :#これ以上深く潜れない場合。最大レベルの全文字列におけるカウントを実行、削除して上階へ戻る。
                now_level = tree.pop()
                for node in now_level :
                    if node.is_palindrome_count(K) :
                        count +=1
                return count
            tmp_node = tree[-1].pop()#Nodeが存在するが、不完全でまだ深く探索できる
            tree.append(tmp_node.create_next_level_by_finally_Node())
            count = tree_search(count)             
        tree.pop()
        return count
        
    #探索の開始
    result = tree_search(0)
    print(result)
    return

from itertools import permutations
from more_itertools import distinct_permutations

def main3() :
    N, K = map(int, input().split())
    S = list(input())
    result = 0
    for p in set(permutations(S)) : 
        if is_palindrome(p, N, K): result += 1
    print(result)

def is_palindrome(string, N, K) -> bool:
    for i in range(N-K+1) :
        s = string[i:i+K] 
        if s == s[::-1] :
            return False
    return True

def main4() :
    N, K = map(int, input().split())
    S = list(input())
    result = 0
    for p in distinct_permutations(S) :
        if is_palindrome(p, N, K): result += 1
    print(result)
    return
    
        
if __name__ == "__main__" :
    main4()
