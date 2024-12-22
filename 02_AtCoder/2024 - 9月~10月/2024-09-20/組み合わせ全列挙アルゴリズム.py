""" #####################################################
発想

5本の指で示せるサインの総種類数を求めよ

result = 

N
σ   NCi
i=0

である。

NCi
N * N-1 * 
---------
1 * 2 * 

n! / (N-i)!
n!



---------------------------------------------
main2, main3の話
もし、全ての指に区別がつく場合、
答えは2^Nとなる。これは繰り返し二乗法に帰着しそう。
つまり、O(logN)で答えが求められそう



-----------------------------------------------
main4の話。
もし20指の数に上限指定があり、20本だったら? →作成できるかもしれない。
dp[次の親指]

ここで、必ず20先なのか?という疑問が生じる。
文字列で判別する際。
nyaa を判別する際、この先zは存在するのか?という話になる。
今回の問題に置き換えると、親指を選べる状態か否か(親指の有無)を判定することに近い。
つまり、各指の欠損を確認するだけで問題を解くことが出来そう。
もし指の有無も考慮することができると、指が無い人を含めたサイン量も含めて調べることが出来そう。
?

##################################################### """
import math
import time

def cheaker() :
    N = 5
    for i in range(N) :
        print(math.factorial(i))
    return

def check_factorial_order() :
    """ N!の計算量を出力する
    
    
    MEMO - 
    i = 3499 で0.1秒を超えた。
    i = 3428 で0.1秒を超えた。
    
    MEMO 2
    print時間を抑えると、
    i = 11482 で0.01秒を超えた。
    i = 9967 で0.01秒を超えた
    """
    SHOW_FACTORIAL = False
    TIME_BORDER = 0.01 #1回の計算の制限時間
    
    max_num = 10**5
    for i in range(max_num) :
        t = time.time()
        result = math.factorial(i)
        if SHOW_FACTORIAL : print(result)
        t2 = time.time() 
        
        if i % 100 == 0 : print(f"現在i={i}, 所要時間t={t2 -t}")
        if t2 - t > TIME_BORDER : 
            print(f"現在i={i}, 所要時間t={t2 -t}")
            return #計算時間が0.1秒を超えたら終了する
    return 

def check_mypow_order() :
    """ 繰り返し二乗法の計算時間を出力するアルゴリズム 
    
    MEMO
    ---------------------
    1. 現在i=62825, 所要時間t=0.032913923263549805
    2. 現在i=135202, 所要時間t=0.03490591049194336
        現在計算できた文字の桁数は40700桁です。
    ※2は1と違って途中までパソコン操作を放置しました。高速に計算された結果長い間耐えたってだけです。
    """
    
    SHOW_FACTORIAL = False
    TIME_BORDER = 0.01 #1回の計算の制限時間
    BASE_NUM = 2 #乗数の底
    
    
    max_num = 10**8
    for i in range(max_num) :
        t = time.time()
        result = mypow(BASE_NUM, i)
        if SHOW_FACTORIAL : print(result)
        t2 = time.time() 
        
        if i % 10000 == 0 : print(f"現在i={i}, 所要時間t={t2 -t}")
        if t2 - t > TIME_BORDER : 
            print(f"現在i={i}, 所要時間t={t2 -t}")
            print(f"現在計算できた文字の桁数は{len(str(result))}桁です。")
            return #計算時間が0.1秒を超えたら終了する
    return 

def main() :
    """ 組み合わせの総数を出力するアルゴリズム。 
    
    組み合わせの公式を用いて、最もシンプルな実装。
    計算量。O(N(1~Nまでfor文合算値) * (N(階乗) + N + N)) = N*3*N = N^2処理。 
    1 ~ 10**4くらいまで求められる?
    
    もしくは、N! の計算量が N!であるとき、 N * N! で非常にひどい状態。
    40位までしか計算できないはず。
    
    """
    N = int(input())
    result = 0
    for i in range(N+1) :
        result += math.factorial(N) / math.factorial(N-i) / math.factorial(i)
        print(f"{i}種類の時、組み合わせ総数は、{result}")
    return


def main2() :
    """ 動的計画法を使用して、部分文字列の総種類数の出力を目指すアルゴリズム。 
    
    今回の問題は、全ての指が違うオブジェクト(a~b)ではないということがとても重要。
    もしくは、問題文を右手の人差し指から、左足の小指までという20種類の指という制約を設けるかで話が変わってきそうである。
    
    今回の問題は、全て指で誰の何か決まっているバージョンとする。
    →次の、indexを記す
    
    加算するindexは、最も左側に位置するindexであり、dp[i], 1~i~N である。
    基本この動的計画法は O(N)だが、今回は全てが別オブジェクトになるため、O(N^2)になる。
    
    ...あれ？
    この問題って 人差し指を表示するか否か、この使用するか否かという話じゃない？
    あれ？この数って 
    指が1本なら 2^1 = 2通り
    指が5本なら 2^5 = 32通り
    """
    N = int(input()) #指の本数
    
    dp = [0 for i in range(N+1)]
    dp[0] = 1
    for i in range(N) :
        for j in range(i+1, N+1) :
            dp[j] += dp[i]
    print(dp)
    print("----------------")
    print(sum(dp[1:]))
    return

def main3() :
    """ 任意の数a, b が与えられます。 a**bを導出せよ
    繰り返えし二乗法を用いて実装する。
    
    乗数を計算する。
    """
    a, b = map(int, input().split())
    ans = mypow(a, b)
    print(ans)
    return
    
def mypow(x, n:int) :
    """ 繰り返し二乗法 (myfunction), xが低, nが乗数 
    
    nをビット化して算出すればなかなかよりよい実装だが、今回は無視する。
    +αの要素であるため。
    """
    if x==0 : raise ValueError("底に0を指定しないでください。")
    SHOW_CALC = False
    result = 1
    while n > 0 :
        if SHOW_CALC : print(f"x:{x}, n:{n}")
        if n % 2 == 1 : result *= x 
        x, n = x*x, n//2
    if SHOW_CALC : print(f"result:{result}")
    return result  
    
    

if __name__ == "__main__" :
    #check_factorial_order()
    check_mypow_order()
    #main3()
    #cheaker()    
