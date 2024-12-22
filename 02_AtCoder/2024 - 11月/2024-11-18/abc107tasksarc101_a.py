""" #####################################################
発想

0からxi までの距離を移動したとき、つけられるろうそくの本数を記した累積和配列Aを考える。
X = -3,-2,-1,0,1,3 の時
A = {-3:4, -2:3, -1:2, 0:1, 1:2, 3:3}
この時、0の数値が正負どっちにも含まれていることに注意する。
ンで、エスパーポイントだが、
- 右に一回最小距離を行く+左に折り返して進む、
- 左に最小距離を行く+右に折り返して進む 
で要件を達成して終了する可能性が高く、
何度も左と右を行ったり来たりすることはないだろう。

→すると、累積和の組み合わせとして、K=4の時
Xを0 まで行って1本付けて、-3までつけに行く
Xを1 まで右行って2本付けて、-2までつけに行く
Xを-1 まで左行って2本付けて、+3までつけに行く
の3通りしか考えられなくなる。
この全数量として、O(N-K+1) の調査で問題なさそう。→これでいこう

上記の調査をするとき必要な条件分岐(xi1 を左方向、xi2を右方向とする)
- xの絶対値条件
    - |xi1| < |xi2| : 左から調査
    - |Xi1| > |xi2| : 右から調査
    が必要である。
- xi1, xi2の固定について
    - 全数調査なので、xi_1 を最も左の位置から、ずらし、xi_2が最も右の位置に来るまで作業する。
    
- DB構造
    - 今回新たに、 xi_1 の累積indexと、xiの位置を格納するDB構造として
        - negative_x = [0, 0, -1, -2, -3]
        - positive_x = [0, 0, 1, 3]
        配列を定義して使用する。
        1. negative_x をN-1から0(forで-1)まで実行する
        2. positive_x の見る位置は一意に定まっているので、xを調査する
            xi_1 = 4の時K=4からxi_2=0 を見ればいい。
            ※コーナーケース、negative_xがK以上の時を注意する。なので、for分で min(K, N-1)とする
            残りの見るべき数 = K-i
##################################################### """
def check() :
    return


def main() :
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    
    negative_X, positive_X = [], []
    for x in X :
        if x < 0:
            negative_X.append(x)
        elif x>0:
            positive_X.append(x)
        else :
            negative_X.append(0)
            positive_X.append(0)
    negative_X.append(0)
    negative_X = negative_X[::-1]
    positive_X.insert(0,0)

    #print(negative_X)
    #print(positive_X)

    result = float("inf")
    for i in range(min(K, len(negative_X)-1), -1, -1): #negativex を使用する分だけ全調査
        if K-i > len(positive_X)-1 :
            break
        if abs(negative_X[i]) > positive_X[K-i] :
            result = min(positive_X[K-i]*2+abs(negative_X[i]), result)
        else :
            result = min(abs(negative_X[i]*2)+positive_X[K-i], result)        
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
