from math import sqrt

def cheaker() :
    return

def main2() :
    """
    ユークリッドの互換法について。

    ＜手法＞
    　大きいほうの数を「小さいほうの数で割った余り」に変更する
    　↓
    　片方が０になったら終了する
　　　　という手法

    432 117
    ↓ 432 / 117 = 3...81
    81 117
    ↓ 117 / 81 = 1...36
    81 36 
    ↓ 81 / 36 = 2...9
    9 36 
    ↓ 36 / 9 = 4...0
    9 0 

    答え　「9」　となる。

    理由：操作を行っても「最大公約数が変更されない」という法則性があるから。
        432 - 117 → 9
        117 -  81 → 9
        ...

    #################################################################
    なぜ？最大公約数が変更されないのか？（自分の考察）
      a = b * 割数 + 余り
      aにbの公約数となる数が含まれているのなら、
      　余りの部分にも公約数が含まれれば
      　3の倍数（b*任意x）+3の倍数（余り）=3の倍数(a)
      と書くことができる。


      要するに、「共通した倍数」を持つ数たちの傾向をうまく活用したってこと。
    #############################################################
      
    計算量
    　余り < 2/3
    　という特性より

      O(log(A+B))
　      となるらしい。
    """
























def main() :
    """答えを見ないでやってみる。

    手法
    大きいほうをsqrt(x)まで全探索。
    　→A(List)に記載
    　　O(√x)
    Aに対応した数を乗数を追加
    　→Aの全因数をメモ
        O(+√x)
        ※順序に注意
        
    小さいほうをさっき作成したメモで割り切れるか判定。
    　  O(+2√x)
    結果想定される計算量
    　O (4√x)　= O(√x)
    
    
    """
    def create_facter_list(x) :
        """与えられた数の全因数を格納したリストを返す関数

        Parameter
        -----------
        x : int
            因数を求めたい数

        Return
        --------
        f_list : list
            全因数を纏めたリスト
        """
        f_list = []
        for i in range(1, int(sqrt(x))) :
            if x % i == 0 :
                f_list.append(i)
            else : pass

        for i in range(len(f_list)-1, -1, -1) :#後続に対応する数の追加。
            f_list.append(int(x / f_list[i]))
            
        return f_list
            
    def Exploration(x, List) :
        """変数xは、与えられたリストの因数を持つのかどうかを判定

        Parameters
        ------------
        x : int
            判定したい数
        List : list(int)
            このリストに入っている数を検証する。

        Return
        ---------
        int
            因数の最大量
        """
        for i in range(len(List)-1, -1, -1) :
            if x % List[i] == 0 :
                return List[i]
            else : pass
        return List[i]


    #Main
    S = list(map(int,input().split()))
    S.sort()

    #大きいほうの数の因数をメモする
    List = create_facter_list(S[1])

    #小さいほうの因数を探索する
    print(Exploration(S[0], List)) 
      
    return


if __name__ == "__main__" :
    main()
    #cheaker()
