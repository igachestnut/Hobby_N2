""" #############################################
尺取り法を実装してみよう! のコーナー

https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_m


異なる整数ペアのうち、
K以下になる選び方はなんとおりか、

尺取り法とは
01 -リストをソート
02 -右から順に実行
03 -成り立つ最大の数まで調査⇒終了
04 -次の数へ移動
05 -調査した最終位置から調査してうまくいくかどうか調査

調査回数(計算量) O(N)
一度調査し、Trueだった場所はもう二度と操作しない為。
順番も左から順番でいいため。



使用にあたる注意点
(1) 参照位置どおしの距離を、必ず1以上離すこと (for文で回す量もちょっと少なくなる)
(2) _tmp_end (後ろの調査する配列)の位置は配列の長さ以上にならないようにすること


################################################ """

def cheaker() :
    return


def main() :
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    result = 0
    _tmp_end = 0
    for n in range(N-1) :#2つのペアの調査アルゴリズム自体は最後から-1までで良い。(最低2つ数値が必要)
        # 入力チェック もし一緒なら調査する位置の操作を次のindexにする。
        if n == _tmp_end :
            _tmp_end += 1
        
        # 一致する最大尺の調査
        while _tmp_end < N and abs(A[n] - A[_tmp_end]) <= K : #現在位置が正しい状態なら次の調査(次が正しいとは限らない)
            _tmp_end += 1
        #この状態で設定されている_tmpは、初めてうまくいかない状態のindex
        #つまりうまくいく場所は_tmp_end-1である。
        
        # 結果の記入
        result += abs((_tmp_end-1) - n)#存在する要素数、(A[n](index=n番の時のAの組み合わせは何通りか )要素が1離れていると1通り、要素が2離れていると2通り)
        #print(f"現在の配列状況:{A[n:_tmp_end]}")
        
    print(result)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
