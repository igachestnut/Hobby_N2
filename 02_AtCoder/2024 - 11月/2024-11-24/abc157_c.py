""" #####################################################
発想


- N 桁
- Si桁目がciである。

- -1というケース。
    - 与えられたMのうち、同じ桁に違う数が存在するならダメ。


    
...もしかして、
N=3 で3桁目が9だった時、
答えは109ではなく、9と答えを出さなければならないってこと?
##################################################### """
def check() :
    print(0*0) #0と返される。
    return


def main() :
    N,M = map(int, input().split())
    result = [-1 for i in range(N+1)] #桁数をindex: -1はNodataの意味
    for i in range(M) :
        s,c = map(int, input().split())
        if s==1 and c==0 :
            print(-1)
            return
        elif result[-s] == -1 or result[-s] == c:
            result[-s] = c
        else :
            print(-1)
            return
        
    if result[-1] == -1 :
        result[-1] = 1
    for i in range(N) :
        if result[i] == -1: result[i]=0
    
    print(sum([result[i]*10**(i-1) for i in range(1, N+1)]))
    return

def main2() :
    N,M = map(int, input().split())
    SC = []
    for i in range(M) :
        SC.append(list(map(int, input().split())))
        if N>1 and SC[i][0] == 1 and SC[i][1]==0:
            print(-1)
            return

    for ints in range(10**N) :
        tmp_s = f"{ints:03}"[(3-N):]
        #print(tmp_s)
        result = True
        for [s,c] in SC :
            if tmp_s[s-1] != str(c) : result=False
        if result :
            print(int(tmp_s))
            return
    else:
        print(-1)
    return
        

def main3() :
    N,M = map(int, input().split())
    result = [-1 for i in range(N+1)] #桁数をindex: -1はNodataの意味
    for i in range(M) :
        s,c = map(int, input().split())
        if N>1 and s==1 and c==0 :
            print(-1)
            return
        elif result[-s] == -1 or result[-s] == c:
            result[-s] = c
        else :
            print(-1)
            return
        
    if result[-1] == -1 :
        if N==1 : result[-1] =0
        else : result[-1] = 1
    for i in range(N) :
        if result[i] == -1: result[i]=0
    #print(result)    
    print(sum([result[i]*10**(i-1) for i in range(1, N+1)]))
    return

if __name__ == "__main__" :
    main3()
    #check()
