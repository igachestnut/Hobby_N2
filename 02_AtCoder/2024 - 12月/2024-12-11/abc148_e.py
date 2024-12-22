""" #####################################################
発想

f(n) = 1 (n < 2)のとき
f(n) = n*f(n-2) (n >= 2)の時

- f(0) = 1
- f(1) = 1
- f(2) = 2*(f(0)) = 2
- f(3) = 3*(f(1)) = 3
- f(4) = 4*(f(2)) = 4*2 = 8
- f(5) = 5*(f(3)) = 5*3 = 15
- f(6) = 6*(f(4)) = 6*8 = 48
- f(7) = 7*(f(5)) = 7*15=105

- 0<=N<= 10**18
dp でNの個数だけ記載していく計算方法は使えない。
最低でもlogNくらいにしないと???

...傾向分析
- Nが奇数の時、出現するf(n)のnは必ず全部奇数になる
- Nが偶数の時、　同様に(f(n))のnは必ず偶数になる。
- f(n) が偶数の時、掛け合わされる合計というのは、
    -f(2) = 2*(f(0))
    -f(8) = 8*6*4*2*(f(0))になりそう
    ここだけ見ると N! の一つとびバージョンですね。
- f(8) を素因数で分けると
    - 2**3 2**1*3**1 2**2 2**1 
    - 2**7 * 3**1

- 今回の問題は末尾に何個の0が続くか→何回2*5 が作られるか
- すると奇数の問題はどんなに頑張っても0は生じることはない。

- んで.5が出てくる回数→
f(10) = 5*1
f(20) = 5*1
f(30) = 5*1
f(40) = 5*1
f(50) = 5*2
f(60) = 5*1
f(70) = 5*1
f(100)= 5*2
f(110)= 5*1

...エスパーポイントだが、10を構成するには2*5 だが 出現するは 2>>5 になっていそう。
なので、5の出現回数だけ調査する?
まだ現在線形時間で探索するので O(N/10)くらいです

- 傾向分析2
- f(i) iの末尾が 10~40, 60~90 のとき、必ず5*1である
- f(i) iの末尾が 50 の時必ず5**2(先頭が5の時、5の回数が1多くなる)
- f(i) iが10, 100, 1000 のようになっているとき、0が繰り返された回数分だけある。
... すると
f(10~100)までの数値と、f(110~190)までの出現回数って一緒?
f(510~550) は?一緒らしい。
微妙に条件が変わる(f(250),f(500),f(750))から、iの末尾が 10~40, 60~90 のとき、必ず5*1であるを使用するべき
- N= 12340 だった場合、j=2桁目の40を抜いた数値→12300になり、
この時のf(10~40,60~90)の出現回数は 8*123 回ってこと??になりそう。
したがって、N=12340の時 8*123 + n2%10 (if n2=10~40 else n2%10-1)
あとは50,100,150,といった5の倍数の時
- 50,250,

f(50) = 5*5*2
f(100)= 5*5*2*2
f(150)= 5*5*2*3
f(200)= 5*5*2*4
f(250)= 5*5*2*5
...
f(1000)= 5*5*5*2*2*2

dp[1] = 2 (k=1 →50カウント)
dp[2] = 2
dp[5] = 2+1
dp[10]= 2+1
dp[25]= 2+2 = (1250)
dp[125]= 2+3 = 


f(1~100)までの5の出現回数
(f(10)~f(40)4回+ f(50)2回 + f(60)~f(90) の4回)の計10 + f(100)の2回

Nの桁数j(1~18)の時の数値がnjだった場合
nj = 2, j = 2 だった場合 N=20

答えは、入力値N 各njにおける足の出た分の5の回数 + 足が出なかった分の5の回数

55 → 50, 4 → 
    50 = 1+1+1+1+2回
    4 = 0回

54 
    = f(10) * f(20) ,,, f(50)
550 = f(10) * ... f(540) * 550



i10, 5count1
i20, 5count1
i30, 5count1
i40, 5count1
i50, 5count2
i60, 5count1
i70, 5count1
i80, 5count1
i90, 5count1
i100, 5count2
i110, 5count1
i120, 5count1
i130, 5count1
i140, 5count1
i150, 5count2
i160, 5count1
i170, 5count1
i180, 5count1
i190, 5count1
i200, 5count2
i210, 5count1
i220, 5count1
i230, 5count1
i240, 5count1
i250, 5count3
i260, 5count1
i270, 5count1
i280, 5count1
i290, 5count1
i300, 5count2
i310, 5count1
i320, 5count1
i330, 5count1
i340, 5count1
i350, 5count2
i360, 5count1
i370, 5count1
i380, 5count1
i390, 5count1
i400, 5count2
i410, 5count1
i420, 5count1
i430, 5count1
i440, 5count1
i450, 5count2
i460, 5count1
i470, 5count1
i480, 5count1
i490, 5count1
i500, 5count3
i510, 5count1
i520, 5count1
i530, 5count1
i540, 5count1
i550, 5count2
i560, 5count1
i570, 5count1
i580, 5count1
i590, 5count1
i600, 5count2
i610, 5count1
i620, 5count1
i630, 5count1
i640, 5count1
i650, 5count2
i660, 5count1
i670, 5count1
i680, 5count1
i690, 5count1
i700, 5count2
i710, 5count1
i720, 5count1
i730, 5count1
i740, 5count1
i750, 5count3
i760, 5count1
i770, 5count1
i780, 5count1
i790, 5count1
i800, 5count2
i810, 5count1
i820, 5count1
i830, 5count1
i840, 5count1
i850, 5count2
i860, 5count1
i870, 5count1
i880, 5count1
i890, 5count1
i900, 5count2
i910, 5count1
i920, 5count1
i930, 5count1
i940, 5count1
i950, 5count2
i960, 5count1
i970, 5count1
i980, 5count1
i990, 5count1
i1000, 5count3

...10 の倍数なら必ず1
...50の倍数なら必ず2
...250の倍率なら必ず3
...1000の倍数なら必ず4
##################################################### """
def check(N=1500) :
    
    tmp_m = N%5
    result = 0
    while tmp_m == 0 :
        result += 1
        N //= 5
        tmp_m = N%5
    #print(result)
    return result

def checkmain() :
    #main()
    for i in range(10, 1010, 10) :
        r = check(N=i)
        print(f"i{i}, 5count{r}")

def checkmain2() :
    """ 5の出現回数の合計 """
    result = 0
    for i in range(10, 12310, 10) :
        if i %50 == 0 :continue
        result += check(i)
        print(result)
    print("---------------")
    print(result)

def check2() :
    print(984//8)

def main() :
    N = int(input())
    if N%2 == 1:
        print(0)
        return
    N = N//10 
    result = N
    while N>0 :
        N = N//5
        result += N
    print(result)
    return


if __name__ == "__main__" :
    main()
    #checkmain()
    #check2()
