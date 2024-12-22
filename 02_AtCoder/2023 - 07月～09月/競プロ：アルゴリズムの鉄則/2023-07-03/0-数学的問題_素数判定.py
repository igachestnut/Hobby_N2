from math import sqrt

def cheaker() :
    return




















def main() :
    """
    与えられた整数は素数かどうかを判定するプログラム

    傾向に就いて考える
    例)
      111
      111 / 2 = 55.5
      111 / 3 = 37.0
      111 / 4 = --- #2の倍数だから考える必要なし
      111 / 5 = 22.2
      111 / 7 = 13.875
      111 / 11 = 10.9
      111 / 13 = 8.5

    １.素数判定、111 % (x)
      x >= 111/2
       の場合は判定する必要なし。理由：必ず割り算の値は1以上2未満になるから。

    ２.素数判定　111 % (x)
      x >= sqrt(111)までやる必要なし？
      　理由：111の因数分解をするにあたって、ある2つの値p,qが出るとき、
      　　p <= q　の際、必ず p < sprt(111) and q >= sqrt(111)
      　　となる。

      111→Aとすると
      →以上より、for分を1～sqrt(A)+1となる（sqrt(1)の余りが０の場合があるため）ところまで判定すると、
      　素数かどうかを判断できる。

    ３.素数判定で、4,6,8.9は判定しなくていいんじゃないか問題
    　だって、2の倍数や3の倍数なんだもん。これが削減されればもっと早い？

　　　メモしていく手法
　　　　sqrt(A)までの長さのrange()を作成する.
        2で割る。→全てにメモする。
        3で割る。→全てにメモする。
        4で割ろうとするが、既に計算済み→passする。

        →この手法は、エラトステネスのふるいという手法らしい。
        俗に言う、素数だけ判断していこうの手法。


    ###################################################
      ２.の手法だけ適用した場合、
        1～sqrt(A)+1
          計算量O(N * sqrt(A))

    
    """
    
    def create_prime_list(x) :
        """#素数を格納したリストを作る関数
        
        Parameters
        -----------
        x : int
            判定したい数
        
        len_list : int
            判定しなければならない数の最大数→sqrt(x)

        Return
        -----------
        _list : list
            素数だけがFalseな状態のリスト
            
        """
        #最大長さの算出
        len_list = int(sqrt(x))
        
        #素数を記載するリスト
        _list = [False for i in range(len_list+1)]

        #素数のみのリストを作成
        for i in range(2, len_list) :
            if _list[i] == True : pass
            else :
                #後続の倍数のindexを全てTrueにする。
                for j in range(i+i, len_list, i) :
                    _list[j] = True
        return _list

    #素数判定を行う関数
    def jugde(x, List) :
        for i in range(2, len(List)) :
            if List[i] == False :#まだ判定していない場合
                if x % i == 0 :
                    return "No"
            else :
                continue
        return "Yes"
        
    #Main
    Q = int(input())#試行回数

    for _ in range(Q) :
        x = int(input())

        #素数だけ記載したリストを返す
        List = create_prime_list(x)
        #print(List)

        #判定
        print(jugde(x, List))  
    return





def main2() :
    #エラトステネスの方式を使わないと？
    #素数判定を行う関数
    def jugde(x, List) :
        for i in range(2, len(List)) :
            if List[i] == False :#まだ判定していない場合
                if x % i == 0 :
                    return "No"
            else :
                continue
        return "Yes"
        
    #Main
    Q = int(input())#試行回数

    for _ in range(Q) :
        x = int(input())
        List = [False for i in range(int(sqrt(x)+1))]
        #判定
        print(jugde(x, List))  


def main3() :
    #入力　1000000000000001 : 10**16+1
    #さらにリストを作らない形式だと？
    def jugde(x) :
        for i in range(2, int(sqrt(x)+1)) :
            if x % i == 0 :
                return "No"
            else :
                continue
        return "Yes"

    Q = int(input())
    for _ in range(Q) :
        print(jugde(int(input())))

        



if __name__ == "__main__" :
    #main()
    #main2()
    main3()
    #cheaker()
