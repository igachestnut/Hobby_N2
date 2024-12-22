def cheaker() :
    return


def main() :
    H, W = map(int,input().split())
    Map = []
    start = []
    end = []
    
    #エネルギーを記載するためのMap作成
    for i in range(H) :
        A = list(map(str, input().aplit()))
        for j in range(W) :
            if A[j] == "." :
                Map.append(0)
            elif A[j] == "#" :
                Map.append(-1)
            elif A[j] == "S" :
                Map.append(0)
                start.append(i,j)
            else :
                Map.append(0)
                end.append(i,j)
    
    #薬情報のまとめ      
    N = int(input())
    for i in range(N) :
        R, C, E = map(int, input().split())
        Map[R,C] = E
        
    #最後だけ薬は使用しない為除外
    Map[end[0], end[1]] = 0
    
    
    #最初から経路を行ける場所を全探索しつつ、
    #以下の条件で再調査を実施する。
    
    
    
    return

def search(i,j) :
    """ 与えられた場所から行くことが可能な場所を全探索する
    
    MEMO
    -------------
    (1) 薬>そこに到達した時点でもENERGYだった場合
        その地点から再調査をしたい。
        search(i, j)
    (2) それ以外、行けうる場所を幅優先探索でリストを保持して、
        そのリストが無くなるまで調査を実施するとか？
        
    
    """
    pass

if __name__ == "__main__" :
    main()
    #cheaker()

""" 解説のまとめ

有効グラフの作成。
BFSを適用して行う。
それでいい

BFSの実装方法について。

"""