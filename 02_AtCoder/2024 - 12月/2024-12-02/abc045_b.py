""" #####################################################
発想

- 制約
    - Aから始まる
    - カードを持っているなら、先頭を捨てる。→その後書いてある人が行動する。
    - カードをすべて消費するまで3人で繰り返す。

- query処理
    - 現在の位置を位置を更新し続ける。

##################################################### """
def check() :
    return


def main() :
    sa = list(input())
    sb = list(input())
    sc = list(input())
    S = [sa[::-1], sb[::-1], sc[::-1]]
    i = 0
    while S[i]: i = ord(S[i].pop()) - ord("a")
    if i==0 :print("A")
    elif i==1: print("B")
    else: print("C")
    return


if __name__ == "__main__" :
    main()
    #check()
