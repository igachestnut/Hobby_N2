""" #####################################################
発想


- 異なる2ボールで,同じ番号をとる方法の総数
- k番目において、自身を取り除いたとの総和を考えたい。
- では、とりあえず、k=1, 2~N番目のボールにおいて、取り出す方法の全列挙
    - ある番号 の取り出し方 N(N-1)//2 通り

- 1~N が使える場合の、取り出し方を全列挙。
    defaltdictに値を追加する。
- 使えるボール数がそれぞれの番号で1減ったときの組み合わせの変化を考える
    2→1 の時、1とおりから0通りになる。
    3→2 の時、3通りから1通りになる。
    -N(N-1)//2 + (N-1)*(N-2)//2
    = -(N-1)  ...(N>0の時)
    になる。計算するNは常に存在しているため、N>0 である。
 
##################################################### """
def check() :
    return

from collections import defaultdict
def main() :
    N = int(input())
    A = list(map(int, input().split()))
    comb_counts = defaultdict(int)
    for a in A: comb_counts[a] += 1
    result = 0
    for value in comb_counts.values() :
        result += value*(value-1)//2
    
    for i,a in enumerate(A) :
        print(result-(comb_counts[a]-1))
    return

def main2() :
    N = int(input())
    A = list(map(int, input().split()))
    c, r = defaultdict(int), 0
    for a in A: c[a] += 1
    for v in c.values(): r += v*(v-1)//2
    for a in A: print(r-(c[a]-1))
if __name__ == "__main__" :
    main()