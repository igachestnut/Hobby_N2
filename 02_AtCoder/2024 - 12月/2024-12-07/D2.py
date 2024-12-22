""" #####################################################
発想

- 自然数N を素因数分解したときの各因数の指数を用いて、
約数の個数は(a+1)(b+1)...(i+1)と定義できる

今回の出したい答えは、
約数の個数=9 より、
a=8, の時
a=2, b=2 の時
しか存在しない。

a=8 は
任意の素因数をqとすると
- q^8 が素因数以内かどうか判断すればよい。

a=2, b=2は
任意の素因数をq,pとすると
- q^2 * p^2 がNを超えないかどうか判断すればよい。
(注意、q,pは素因数なので2以上の数値)

- 計算量は、p^2 より、
最大Nに対し、て最低p^2 することから sqrt(N)だけ作業するとよい。
=2*10**6 まで。

p,q をかぶりなしで定義していくとなると、
q = 2~sqrt(N)-1
p = q+1~sqrt(N)
までずらして調べるとよいが、、、
このままでは計算量がO(sqrt(N)^2)になってしまう

q^2 * p^2 をしてN以下の最大を見つける
q = 2で l=1で
p = 3で r=2 が該当数のmaxだった場合、
r-l で1通り
p = 5で r=3 の時
lが1と固定していることを考慮すると、
2,3 2,5 の2通り r-l で大丈夫そう。
r の位置を最大からだんだん小さくしていく方針のほうがよさそう。(qが増、pの値は単調減少になるため)


...あとN以下の数値における素因数を列挙するプログラムが欲しい。
エラトステネスの篩

##################################################### """
def check() :
    return

import math
def main() :
    """ 何かが違うけど、原因がわからない """
    N = int(input())

    # エラトステネスの篩でsqrt(N)までの素数を全列挙
    is_prime = [True for i in range(int(math.sqrt(N))+1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(int(math.sqrt(len(is_prime)))+1) :
        if not is_prime[i]: continue 
        for j in range(2*i, len(is_prime), i) :
            is_prime[j] = False
    prime_numbers = []
    for i,p in enumerate(is_prime) :
        if p:
            prime_numbers.append(i)
    #print(prime_numbers)

    # 約数が9の時の数の数え上げ。 1.q^8 の数え上げ
    result1 = 0
    tmp_q = 2
    while tmp_q**8 <= N :
        result1 += 1
        tmp_q += 1
        #print(tmp_q)
    
    # 2. p^2*q^2 の数え上げ
    result2 = 0
    l,r = 0, len(prime_numbers)-1 #※l,rは左、右の意味 resultではない。
    while l<r :
        if prime_numbers[l]**2 * prime_numbers[r]**2 > N :
            r -= 1
            continue
        #print(prime_numbers[l], prime_numbers[r], prime_numbers[l]*prime_numbers[r])
        result2 += r-l
        l += 1
    
    result = result1+result2
    print(result)
    return

def check() :
    #print(36**8)
    a = list(range(201))
    for i in range(3, len(a), 3) :
        print(a[i])

import math
def main2() :
    N = int(input())

    #print(int(math.sqrt(N)))
    #print(int(math.sqrt(N)+1))
    #print(int(math.sqrt(int(math.sqrt(N)))))
    #print(int(math.sqrt(int(math.sqrt(N))))+1)

    # エラトステネスの篩でsqrt(N)までの素数を全列挙
    is_prime = [True for i in range(int(math.sqrt(N))+1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(int(math.sqrt(len(is_prime)))+1) :
        if not is_prime[i]: continue 
        for j in range(2*i, len(is_prime), i) :
            is_prime[j] = False
    prime_numbers = []
    for i,p in enumerate(is_prime) :
        if p:
            prime_numbers.append(i)
    #print(prime_numbers)
    #print(len(prime_numbers))

    # 約数が9の時の数の数え上げ。 1.q^8 の数え上げ
    result1 = 0
    tmp_q = 2
    while tmp_q**8 <= N :
        result1 += 1
        tmp_q += 1
        #print(tmp_q)
    
    # 2. p^2*q^2 の数え上げ
    result2 = 0
    l,r = 0, len(prime_numbers)-1 #※l,rは左、右の意味 resultではない。
    while l<r :
        if prime_numbers[l]**2 * prime_numbers[r]**2 > N :
            r -= 1
            continue
        #print(prime_numbers[l], prime_numbers[r], prime_numbers[l]*prime_numbers[r])
        result2 += r-l
        l += 1
    
    result = result1+result2
    print(result)
    return

if __name__ == "__main__" :
    main2()
    #check()
