""" 
N以下の正のうち、
正の約数をちょうど9個持つもの総数

- 正の約数をちょうど9個持つような状態の数はどのようなものがある?
- 36
    - 1,2,3,4,6,9,12,18,36 の9個

- すると、Nがどんなに与えられていたとしても、36がそうであることには変わりがない。
- では条件を満たす正の数はどのようなものがあるのかを列挙しよう。


- 36の例を言い換えると、
    - 36 = p*q で表すことができ、この場合では
    p=1, q=36
    p=2, q=18
    p=3, q=12
    p=4, q=9
    p=6=q

のようになってくれる。これによりいえることは...
- 約数が9個であるということなので、 
条件を満たす数a というものは必ず**2 したら該当数になる(a=sqrt(q)*sqrt(q))
- 1~sqrt(a)までで2回割り切れる数であること


では、1~N まで
- a**2 <= N となる数値を調査する
- それぞれ a**2 を1~a で調査し、 ??? O(2*10**7)
... これから調査をしようとすると、ぎりぎり間に合わなさそう。


- a**2 ということは、
aを因数分解すると、
6 = 2*3 になる。 これは1,2,3???
a の約数は
6 = 1,2,3,6 であるから、6を含めずに、2,3の2つである。
7x
8 = 1,2,4,8 ...64=1,2,4,8,16,32,64 xだめだね
9 = 1,3,9
10= 1,2,5,10...100=1,2,4,5,10
14= 1,2,7,10...196=


.....仮に10**2 が行ける場合、
10が約数となる系のすべての数値は約数がそれ以上になってしまうことが確定するため、
調べてはいけない。 20,30,40,....など。

すると、
ある数値Bにおける約数集合b が 素数であったとき、 
Bよりも大きい数値でかつその素数が含まれている番号は、
ちょうど約数を9つもつ可能性がある




"""
def check() :
    """ N==4*10**12 だった時、2乗してN以下になる数字は何個ある? 
    
    result = 1999999 < 2*10**7
    """
    N = 4*10**12
    result =0
    a = 1
    while a**2 < N:
        result += 1
        a +=1
    print(result)
    return

def check2() :
    """ ある任意の数における約数が日するかどうか """
    D = [0 for i in range(40)]
    for i in range(1,40) :
        for j in range(i,40) :
            if j%i==0 :
                D[j] += 1
    for i in range(4) :
        print(D[i:i+10])

def main() :
    N = int(input())
    result = 0
    tmp_a = 1
    while tmp_a**2 <= N :
        tr = 1
        #print(tmp_a)
        for i in range(2,tmp_a) :
            if (tmp_a**2)%i == 0 :
                tr += 1
        if tr == 4:
            result +=1
        tmp_a+=1
    print(result)
    return

import math
def main() :
    N = int(input())
    query = [True for i in range(int(math.sqrt(N))+1)]
    result = 0
    for i, q in enumerate(query[2:]) :
        if q == False :
            continue
        tr = 0
        for j in range(2,i) :
            if (i**2)%j == 0 :
                tr += 1
        if tr == 4:
            result +=1
            for j in range(i,int(math.sqrt(N)),i) :
                query[j] = False
    print(result)
    return

if __name__ == "__main__" :
    main()
    #check2()
