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
"""

def cheaker() :
    return


def main() :
    N, K = map(int, input().split())
    S = list(input())
    
    #Nodeの作成
    set_S = set(S)
    node_S = [0 for i in range(len(set_S))]
    for i, ss in enumerate(set_S) :
        for s in S :
            if s == ss :
                node_S[i] += 1
    
    #print(node_S)
    s = ""
    result = DFS(s, node_S, K, 0)
    print(result)
    return

def DFS(s, node_S, K, result):
    """ 一つ一つ文字列を作成して調査する。
    
    parameters
    --------------
    - s : string 
        現時点で作成済みのString
    - node_S : list[int] 
        その地点において、次に見えそうな地点。
    - K : stringの長さ。到達地点
    - result :int
        カウント数
    """
    #print("----")
    #print(s)
    #print(node_S)

    #入力された文字列は、完成されているのか確認
    if len(s) == K :
        for i in range(K//2) :
            if s[i] != s[-i-1] :
                return result 
            else :
                pass
        return result + 1

    #作成足りないなら、適宜作成してDFS                
    for i in range(len(node_S)) :
        #nodeで行けない個所は飛ばす。
        if node_S[i] == 0 :
            continue
        
        #新しいindexの作成
        new_s = s + str(i)
        new_node = [j for j in node_S]
        new_node[i] = node_S[i] - 1
        result = DFS(new_s, new_node, K, result)
    
    return result
        

if __name__ == "__main__" :
    main()
    #cheaker()
