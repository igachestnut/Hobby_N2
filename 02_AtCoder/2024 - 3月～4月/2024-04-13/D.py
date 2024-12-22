""" 

間違い

経路を探索しつつ、最短のDFSを実装しようとしたが、
なぜか経路の末尾にいろいろ追加されてしまう問題が発生してしまい、
解くことができなかった。


ここで、D2.pyでは、
    隣接リスト表現
    BFSの実行(最短経路探索であるため)
    と分けて実装をしてみる。
    
    目標は30分間での実装


"""
def cheaker() :
    return


def main() :
    L, R = map(int, input().split())
    
    #経路としてありうるMapを計算する
    queue  = [L]  #現在位置。調査したいと思う位置
    Rkeiro = []   #現在分かるRまでたどり着くまでの経路
    Rdis   = R-L  #Rまでたどり着くのに必要な最短距離
    pdis   = 0    #探索において移動した距離。最初は0(移動していない為)
    
    #最短経路の探索 DFSとはいうものの、アルゴリズム自体は経路を全調査している。
    Rdis, Rkeiro = DFS(R, Rdis, Rkeiro, L, queue, pdis)
    
    #結果の出力
    print(Rdis)
    for i in range(len(Rkeiro)-1) :
        print(f"{Rkeiro[i]} {Rkeiro[i+1]}")
    return

def create_start_index_of_good_lists(l) :
    """ 開始位置lから考えられる
    すべてのijコンビを出力する関数 
    
    Parameter
    -------------
    - l : int
        start位置
    
    Return
    ---------
    - _list : list([i, j], [i, j],,,)
        lからRまでの経路で考えられるすべての経路
    """
    _list = []
    i = 0
    while 2**i < l :
        #ijコンビが整数かどうか確認する。
        if  l % (2**i) == 0 :
            _list.append([i, l//(2**i)])
        else :
            pass
        i += 1
    return _list

def create_end_index_of_good_lists(*args) :
    """ i,j の位置から最終位置(r)を出力する関数 """
    i = args[0]
    j = args[1]
    return 2**i * (j+1)

def DFS(R, Rdis, Rkeiro, now_p, keiro, pdis) :
    """ 現在位置から行ける場所を全調査、たどり着いたら比較して保持
    
    Parameters
    -----------
    - R : 最終目標地点
    - Rdis : 最終目標地点までに使用した、現在最速の距離 distanceの意
    - Rkeiro : 最終目標地点までの経路
    
    - now_p : 現在の位置。now positionの意
    - keiro : 入力now_pにおける経路
    - pdis  : その経路の全距離(position distanceの意)
    
    Return
    ---------
    - keiro : list(int,,,)
        たどり着くまでの経路
    """
    #print(f"現在の調査可能性 : {keiro}")
    
    #もし現在位置にいる経路が最速である場合,情報更新
    if now_p == R and pdis < Rdis :
        Rdis, Rkeiro = pdis, keiro
        print("最速情報の更新をしました")
        print(f"Rkeiro : {Rkeiro}")
        return Rdis, Rkeiro
    else :
        pass
        
    #現在位置からの経路取得
    queue = create_start_index_of_good_lists(now_p)

    #もし探索先が存在しない場合、現在の最速を出力して終了
    if not queue :
        return Rdis, Rkeiro
    else :
        pass
    
    #以下queueだけ、一つづつ経路探索
    for q in range(len(queue)) :
        #計算用のindex取得
        [i, j] = queue[q]
        
        #行き先の計算
        _now_p = create_end_index_of_good_lists(i, j)
        
        #行き先がR以上である場合、計算する必要がないため終了
        if _now_p > R :
            continue
        
        #ローカル変数(経過の作成と保持)
        _keiro = keiro        #現在までの経路
        _keiro.append(_now_p) #経路の追加(現地点の情報に更新)
        _pdis = pdis + 1      #最短距離の追加(現地点の情報に更新)
        
        print(f"現在{now_p}に居ます")
        print(f"現在{_now_p}を着目しています")
        print(f"(i:{i}, j:{j} {2**i}+{j+1}={_now_p})")
        print(f"もし{_now_p}を選んだ場合の経路は{_keiro}であり、")
        print(f"経路の距離は{_pdis}です。")
        print("現時点の結果は")
        print(f"Rdis:{Rdis}, Rkeiro:{Rkeiro}です")
        input()
        
        #現地点における調査
        Rdis, Rkeiro = DFS(R, Rdis, Rkeiro, _now_p, _keiro, _pdis)
        
    #調査するだけしたら、最終経路と最終スピードを返す
    return Rdis, Rkeiro
    

if __name__ == "__main__" :
    main()
    #cheaker()
