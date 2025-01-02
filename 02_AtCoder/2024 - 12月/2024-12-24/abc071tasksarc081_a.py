""" #####################################################
発想

- N本の棒。 長さがAi
- 4本を選び、長方形を作る。
作ることができる最大の長方形の面積について

- 長方形なので,並行な辺を2組用意する必要がある。
- 最も大きい順に2つ選ぶ。
- ただし、4本ある場合、それを使う。

##################################################### """
def check() :
    return

from collections import defaultdict
def main() :
    N = int(input())
    A = list(map(int, input().split()))
    bars = defaultdict(int)
    for a in A: bars[a] += 1
    
    result = [0,0]
    ri = 0
    for b in sorted(bars.keys(),reverse=True) :
        if ri >= 2 : break
        elif ri == 1 :
            if bars[b] >= 2 :
                result[ri] = b
                ri+=1
        else :
            if bars[b] >= 4 :
                result = [b,b]
                ri = 2
            elif bars[b] >= 2 :
                result[ri] = b
                ri = 1
    if 0 in result :
        print(0)
    else :
        print(result[0]*result[1])
    return



if __name__ == "__main__" :
    main()
    #check()
