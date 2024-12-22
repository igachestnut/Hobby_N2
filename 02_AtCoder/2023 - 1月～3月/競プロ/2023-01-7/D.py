"""
ある数Nは
p**2,q（それぞれ素数）
で割り切れる。

どんな数になる？という問題。

"""
import sympy as sp
import math

def cheak(pr,N) :
    i = 1
    a = 2
    while True :
        if N % a**2 == 0 :
            break
        else :
            i += 1
            a = pr[i]
    b = N // a**2
    print(a,b)
    return

    
T = int(input())
pr = [i for i in sp.sieve.primerange(1,sp.nextprime(math.sqrt(10**18/2,3)))]
print(pr)
for t in range(T) :
    cheak(pr,int(input()))



a = 1
#この素数の値をどうにかしたい。
#素数で終了することができたら
#ダメ　ンゴ
#sympyを使って素数を格納したリストを生成し動かしていくことを計画したが、
#肝心の素数を作るのに時間がかかってしまうンゴ
#オワタ

#素数を扱わず、log的に割り算を求める。どうすればええの・
#今回二分探索が出来そうにないのも問題ン後。
#O(log(N))の解説がたのしみんご
