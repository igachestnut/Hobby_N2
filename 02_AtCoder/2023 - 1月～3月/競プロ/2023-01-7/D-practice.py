import math

def cheak(S) :
    #試し割法で、最初の割り切りを見つける。
    #→p*p*qで、N<10**18より処理数O(sprt(N,3))である。
    #min(p,q)<=sqrt(N,3)と表せるため。
    
    #必ず初めの数字が分かると残り二つが分かる。

    #最初の数字を見つける
    a = 2
    while True :
        if S % a == 0 :
            break
        else :
            a += 1

    #見つけた数字がpかqか判定する。
    if S % (a**2) == 0 :
        p , q = a ,int(S // (a**2))
    else :
        p , q = int(math.sqrt(S//a)) ,a
    return p,q

#Main
T = int(input())
for t in range(T) :
    S = int(input())
    print(*cheak(S))


