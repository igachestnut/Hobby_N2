""" MEMO

-----------------
- 連続する文字列の選び方 N(N+1)/2 通り
1,2  2,3  3,4  1,2,3  2,3,4  1,2,3,4

余事象を考える?
全体- 満たしていない文字列群

- Idea
もしK,K+1 にて満たしていない配列が存在した場合、
それ以上のすべての要件を満たすことは無い。
1, 2, 3, ..のようにindexを開いていく。
次のindexが超えたとき、それまでのindexは全てOKになる。
頭のindexを次にして、超過の有無を確かめれば。。。

先頭のindexがi1の時に作成できるすべての組み合わせは何通り？
を算出するプログラムを尺取り法で作成することが出来そう。

....WA
もしかしたら問題を読み間違えている可能性があるため、確認してみる。
商品の買い方なので、単体だけでも購入可能ってこと？



main2
...WA
ただ、ACは増えた。
A[i]単体でK以上のケースがあるErrorケースをカバーできたからだと思う。




"""
def cheaker() :
    return


def main() :
    """ 尺取り法で解く 
    
    余剰法ではなく、くくりを作って計算する感じ
    N(N+1)/2の解法は無視している。
    
    WAだった。
    もしかして,A[i]一つでも K以上の可能性があるってこと？だから間違った説がある。
    """
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    result = 0
    i2 = 1 #尺取り法の右側のindex
    tmp_k = A[0]
    for i1 in range(0, N-1) :
        if i1 == i2 : 
          i2 = i1 + 1 #最低でも右側のindexは次の値にしている。
          tmp_k = A[i1]
        while i2 < N and tmp_k + A[i2] <= K :
            tmp_k += A[i2]
            i2 += 1
        #print(f"i1:{i1}, i2:{i2} tmp_k:{tmp_k}, result:{i2-i1 -1}")
        result += i2 - i1 -1
        tmp_k -= A[i1]
    
    print(result+N)        
    return

def main2() :
    """ 尺取り法 + 累積和 """
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    ruiseki_A = [0]
    for i in range(N) : ruiseki_A.append(ruiseki_A[-1]+A[i]) #累積のリストは、0も含める。
    
    result = 0
    i2 = 1 #右側のindex 
    for i1 in range(N) :
        if i1 > i2 : i2 = i1 #もし同じ値以下だった場合、尺取り法の右側indexを強制的にずらさないといけない。
        while i2 < N and ruiseki_A[i2+1] - ruiseki_A[i1] <= K : i2 += 1 #右端に到達するまで or 累積が超えるまで、右側のindexをできるだけ右に送る。OKなら1+する
        result += i2 - i1 
    print(result)
    return

def main3() :
    """ 尺取り法 + 累積和 
    
    買うパターンの加算方法を、A[i]単体でもOKにしたことより、
    i1,i2の初期条件を0,0のように変更する必要がある。
    """
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    ruiseki_A = [0]
    for i in range(N) : ruiseki_A.append(ruiseki_A[-1]+A[i]) #累積のリストは、0も含める。
    
    result = 0
    i2 = 0 #右側のindex 
    for i1 in range(N) :
        if i1 > i2 : i2 = i1 #もし同じ値以下だった場合、尺取り法の右側indexを強制的にずらさないといけない。
        while i2 < N and ruiseki_A[i2+1] - ruiseki_A[i1] <= K : i2 += 1 #右端に到達するまで or 累積が超えるまで、右側のindexをできるだけ右に送る。OKなら1+する
        result += i2 - i1 
    print(result)
    return

if __name__ == "__main__" :
    main3()
    #cheaker()
