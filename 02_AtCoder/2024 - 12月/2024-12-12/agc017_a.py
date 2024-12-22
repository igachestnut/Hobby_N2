""" #####################################################
発想

- 袋の選び方
N = 50
なので、袋の選び方= 2**50

- 奇数か偶数か
- P=奇数の場合
    - 奇数の総数=1,3,5,つの選び方
- P = 0の場合
    - 偶数は何個でもよい
    - 奇数はすべてで1

...まずはビスケットの枚数で重要なのが奇数か偶数かである。
- 奇数か偶数か格納する配列をBとする。
- 0000011111 みたいにできるね
P=1 の時、右1の選び方(合計奇数になるように) * 左0の全部選び方。になり、
P=0 の時、右1の選び方(合計偶数になるように 0も含む) * 左0の全部の選びかた

すると、even の時のビスケットの数をeとしたとき、
選び方の総和というのは
siguma_{i=0~e}(eCi)になる。

odd の時、1,3,...o 一つずつ飛んで選ぶ感じで
P=1なら siguma_{j=P~o+P :(2つずつ飛び)}(oCj)
P=0なら siguma_{j=P~o+P}

では2項定理の場合の、NCx xは0~Nの時の総数を調査するアルゴリズム
...2**N で示せる。
一つ飛びでも、2**N //2 で示せる。
##################################################### """
def check() :
    return


def main() :
    N,P = map(int, input().split())
    A = list(map(int, input().split()))

    # ビスケットの数を偶数奇数に分ける
    even_cnt, odd_cnt = 0,0
    for i in range(N) :
        if A[i]%2 == 0 :
            even_cnt +=1
        else :
            odd_cnt +=1
    
    if P == 1 :
        result = 2**even_cnt * 2**(odd_cnt-1) if odd_cnt != 0 else 0
    else :
        result = 2**even_cnt * 2**(odd_cnt-1) if odd_cnt != 0 else 2**even_cnt
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
