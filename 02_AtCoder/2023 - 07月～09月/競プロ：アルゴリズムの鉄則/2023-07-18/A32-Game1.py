def checker() :
    return


def judge(N, a, b) :
    """先手が勝つかを判定する関数(Incrrectです)

    Parameters
    ------------
    N : int
        スタートの数
    a, b : int
        取ることができる石の数
    
    Return
    ---------
    bool
        先手が勝つならTrue

    Note
    --------
    なぜ間違ったのか？
    　動的計画法でTest問題を確認してみたところ、傾向があることが分かった。
    　しかし、a=1,b=3として扱ってみると、この法則性が合わなかった。

    動的計画法自体が合っているのかという検証が足りない？
    """
    if (N - min(a,b)) % (a + b) < max(a,b) :
        return True
    else :
        return False

def main() :
    """ヒント
    0,1,2,,,とその状態で勝ち状態か負け状態かを
    動的計画法？累積？っぽい考え方でメモしていくと分かりやすいかも？

    """
    N, a, b = map(int, input().split())

    if judge(N, a, b) :
        print("First")
        return
    else :
        print("Second")
        return
    
    return

def judge2(N, a, b) :
    """先手が勝つかを動的計画法を用いて判定する関数

    Parameters
    ------------
    N : int
        スタートの数
    a, b : int
        取ることができる石の数
    
    Return
    ---------
    bool
        先手が勝つならTrue

    Note
    -----------
    動的計画法の手法
    　現在の位置iにおいて、勝つ可能性があるか判定する。
    　残りの石の個数をindexとし、そのindexで勝てるかどうかを記載したListを作成
    　現在の勝てるか必ず負けるかという判定を、i以前の結果から考える
    　indexがNの時の勝つか負けるかの状態を返す　という手法。

    　条件
    　・各プレイヤーは「勝つために最善を尽くす」
    　
　　　負ける条件
　　　　・何もできない（a,bをいずれも引けない状態）　なら負ける
　　　　・a,bのいずれかを引いた先が、両方True
　　　　　→必ず負ける→負け状態 ...①

    　勝つ条件
    　　・a,bのいずれかを引いた先が、片方False　#両方False OK
    　　　→勝つ可能性がある。 ...②

    　※①②の2つで全ての可能性を網羅している  
    以上をまとめると、「必ず負けるかどうか」の判定を行う

    ######################################
    その他注意事項(Listのindexがオーバーフローする話)
    　・n=0の状態で限定的にFalseとわかる
   　 ・nがa以上b以下の時
    　　　aの操作先がTrue→False（勝てない）...(2)
    　　　aの操作先がFalse→True（勝つ可能性あり）
   　 　　（bの操作はしない）
    　・nがa,b以下の時
   　　 　a,bの操作先がTrue→False(勝てない)...(1)
      　　それ以外True
    　オーバーフローする数を操作できない数として定義すると
   　 (1),(2)より、操作できない数がTrueつまり、相手の勝ちという状況を表す
    　　と定義できる。
    　　操作できない→相手勝ち(前位置True)　自分負け（現在位置False）

    　従って、リスト内全てをTrueと定義して作成する。
    """
    #勝つ状態、負ける状態をそれぞれメモするリスト
    List = [True for _ in range(N+1)]
    for i in range(N+1) :
        #何もできないならFalse
        if i < min(a,b) :
            List[i] = False
            continue
        #i番目において、行き先が両方勝ち（必ず自分は負ける）
        elif List[i - a] and List[i - b] :
            List[i] = False
            continue        
        #i番目において、行き先がいずれか負け（勝つ可能性がある）
        else : 
            continue
    #最後に、N (index[N+1])状態を出力する
    return List[-1]


    

def main2() :
    """ヒント
    0,1,2,,,とその状態で勝ち状態か負け状態かを
    動的計画法？累積？っぽい考え方でメモしていくと分かりやすいかも？

    """
    N, a, b = map(int, input().split())

    if judge2(N, a, b) :
        print("First")
        return
    else :
        print("Second")
        return
    
    return


if __name__ == "__main__" :
    main2()
    #checker()
