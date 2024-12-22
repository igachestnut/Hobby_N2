""" #####################################################
発想

- 2つの数 ai>aj をcomb(ai,aj)が最大になるように選んでみる。
- combnationの最大値を取得する。

- N <= 10**5

- 全数調査で全組み合わせを出すとすると、
- N*(N-1)通りある。 =O(N**2)
- ai>aj なので？ aをでかい順にソートすると、
(1,2) (1,3)..(1,N)
      (2,3)..(2,N)
となり, N(N-1)/2 くらいになる。でもO(N**2)

2項定理の表をイメージすると
   n
   0    1
   1   1 1   
   2  1 2 1
   3 1 3 3 1
となっており、当然nが大きいほど答えが大きくなりそう。
また、n/2に近いrのほど値が大きくなりそう。

- rを固定して考える。 ni1 < ni2 の時
comb(ni1,r) < comb(ni2, r)になりそう。逆にこうじゃないケースってある？？？
..rが1の時だけ 同じ値になりそうです。 なので
comb(ni1,r) <= comb(ni2,r)になりそう
...つまり、最大のNを決めれば、それ以外は調査する必要がなさそう。
...すると、Nを最大にして、combnationを求めればいいので、大丈夫。
comb(n,r)は、
N! /r!(n-r)! である。掛け算なので、N回+する作業を考えると、O(N)になってしまう。ダメだね。

...逆に、
Nが固定されているとき、rは最もN/rに近い数値になりそう→bisectで中心を求めるO(logN)
そこからcomb()を導出すれば?


.....いやいや、もうcombnationを導出する必要ないやん。


..ACでした。
分かったこと。
- 2項定理のcomb(n,r)を簡単に導出する方法は無いということ。
- 問題文見てかなり絶望したが、解けるあたりさすがAtcoderですね。とはいえ、このようなアルゴリズムが現実問題必要になったら、、
数学的に正しい証明ができるわけではないためオワタンゴ

##################################################### """
def check() :
    return

import math
import bisect
def main() :
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    if N == 2 :
        result = mycomb(A[-1], A[0])
    else :
        i = bisect.bisect_left(A, A[-1])
        result = 0
        for j in (-1,0,1) :
            if 0 <= i+j < N-1 :
                result = max(result, mycomb(A[-1], A[i+j]))
    print(result)
    return

def mycomb(n,r) :
    """ comb(n,r)を算出するプログラム 
    
    Note
    - おそらく計算量は O(N)
    - factorial(n)がでかいとどうなるかわからんかも。
    """
    return math.factorial(n)/math.factorial(r)/math.factorial(n-r)


def main2() :
    """ combをもう計算しない方向性 """
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    n = A.pop()
    if N == 2 :
        r = A[0]
    else :
        i = bisect.bisect(A, n/2)
        if i == 0 :
            r = A[0]
        elif i == len(A) :
            r = A[-1]
        else :
            #print(A)
            #print(i)
            if abs(A[i]-n/2) < abs(A[i-1]-n/2) :
                r = A[i]
            else :
                r = A[i-1]
    print(n, r)
    return

def check() :
    a = [5,6,7,8]
    print(bisect.bisect(a, 4))
    print(bisect.bisect(a,100))
    b = [0,0,99]
    print(bisect.bisect(b,100))



if __name__ == "__main__" :
    main2()
    #check()
