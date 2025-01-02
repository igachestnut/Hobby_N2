""" #####################################################
発想

- お札の候補を見つけてほしい

- Nは2000枚まで。xyzを構成する全通り? 2000C3 になりそう。 
10**9で多すぎる。

- x,y,z  
- Nの枚数を固定して調査するか、
- 金銭を固定して調査するか??????
....dp???

N = 枚数
金額総和を右にする?

- 遷移を考える
- dp[0][0] = (0,0,0)
- dp[i][j] istrueの時、
    - 次の場所を3つ定義する
    1. +1000円札 dp[i+1][j+1] = 
    dp[i+1][j+1][0] += 1
    2. 5000円札 dp[i+1][j+5] = ...
    dp[i+1][j+1][1] += 1
    3. ...

    - ただし、jが>Yになるなら実施しない。

最後にN枚使い切って dp[N][Y]の値が istureなら出力しよう。

計算量 O(N*Y) O(N*3Y) ...ぎりぎり????
...ダメでした。


x,y,z の決め打ち?
zを1~modYまで決める。10**4である。
これに対して、yを決める。残り、10**4//modY である。
あとはO(1)?

渋沢栄一
津田梅子


##################################################### """
def check() :
    dp = [(0,0,0)]
    print(dp)
    new_dp = dp[-1]
    dp.append(new_dp)
    print(dp)

    add_money = (1,5,10)
    add_noguti = (1,0,0)
    add_higuti = (0,1,0)
    add_yukiti = (0,0,1)
    return

import sys
sys.setrecursionlimit(2*10**6)

def main() :
    """ TLE

    入力例4 2000 2000000 これに1分くらいかかった。OUT

    dp[i+1][j+10] = (t+a for t,a in zip(dp[i][j], add_yukiti))
                                ^^^^^^^^^^^^^^^^^^^^^^^^^
    [Previous line repeated 997 more times]
    RecursionError: maximum recursion depth exceeded
    
    だった。
    """
    N,Y = map(int, input().split())
    modY = Y//10**3
    dp = [[None for j in range(modY+1)] for i in range(N+1)]
    dp[0][0] = (0,0,0)

    add_noguti = (0,0,1)
    add_higuti = (0,1,0)
    add_yukiti = (1,0,0)
    for i in range(N) :
        if i%10 == 0 : 
            print(i)
        for j in range(modY+1) :
            if dp[i][j] == None : continue
            if j+1>modY : continue
            else :
                dp[i+1][j+1] = (t+a for t,a in zip(dp[i][j], add_noguti))
            if j+5>modY : continue
            else :
                dp[i+1][j+5] = (t+a for t,a in zip(dp[i][j], add_higuti)) 
            if j+10>modY : continue
            else :
                dp[i+1][j+10] = (t+a for t,a in zip(dp[i][j], add_yukiti))

    if dp[N][modY] == None :
        print("-1 -1 -1")
    else :
        print(*dp[N][modY])
            
    return

def main2():



if __name__ == "__main__" :
    main()
    #check()
