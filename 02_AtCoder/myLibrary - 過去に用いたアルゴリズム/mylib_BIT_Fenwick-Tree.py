""" #################################################
# BIT (Binary Indexed Tree)  (Fenwick-Tree)の実装

詳細説明は問題解決のideaにあります。

################################################## """

class myFenwickTree :
    """ python用Fenwick-Tree 
    
    Parameters
    ---------------
    - V: list
        Fenwick構造にしたい1次元配列を入力して

    Note
    -------------
    - このクラスのindexは、1~N で制御しています。注意してね
    - クラス定義に必要な計算量O(N loglogN) 
    """
    def __init__(self, V:list, N:int=-1) :
        if N < 0: N = len(V)
        elif len(V) != N :
            print("warning: Nの入力値がlenVと異なっています。確認してね")
            N = len(V)
        
        self._n = N
        self._fenwick_tree = [0] + [v for v in V] 
        x = 1
        while 2**x <= N :
            for i in range(2**x, N+1, 2**x) :
                self._fenwick_tree[i] += self._fenwick_tree[i-2**(x-1)]
            x+=1

    def add(self, i:int, value) :
        """ Fenwick-Treeの任意位置i(1~N) にvalueだけ加減算され、リストを更新する 
        
        Paramters
        -----------------
        - i: int
            - 加算したい位置
        - value: int or float
            - 加算したい数値

        Note
        -----------
        - リスト更新に必要な計算量 O(logN)
        - 加算位置の位置決定方法について
            - 方針: bit制御
            - i & -i で制御。→最も下に立つbit取得(頻出)
            - 更新すべき位置 i += i & -i 
            - ex)
                (0) 0010 1110 の時、
                (1) 0000 0010 =2 を更新, (0)+=(1)  すると 0011 0000になる。
                (2) 0001 0000 
                (3) 0100 0000 
                (4) 1000 0000 が対応
        """ 
        #if i > self._n or i < 0 : raise ValueError("addの入力値が不正です")

        x = i
        while x <= self._n :
            self._fenwick_tree[x] += value
            x += x&-x
        return
    
    def sum(self, i:int) -> int :
        """ 区間[1, i] までの総和を出力する
        
        Parameters
        --------------
        - i: int (1~N)
            - 総和を出力したい量

        Returns
        --------------
        - ans : int
            - 区間の総和

        Note
        ----------
        - 総和を出すための計算量 O(logN)
        - iではなくxを利用している理由。
            - iは取り出したい数値
            - xは加算位置(ずらしていることを表現)
        - 加算する位置に関して、遷移イメージ
            - その地点における、最小bitが立っている場所だけ数を減らしていく。
        """
        ans = 0
        x = i
        while x > 0 :
            ans += self._fenwick_tree[x]
            x -= x&-x
        return ans


def check() :
    N = 100
    V = list(range(100))
    BIT = myFenwickTree(V,N)

    BIT.add(10, 10000)
    for i in range(1, N+1) :
        result = BIT.sum(i)
        print(result)
    print(BIT._fenwick_tree)
    return

if __name__ == "__main__" :
    check()

 
