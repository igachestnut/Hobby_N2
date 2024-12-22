""" #####################################################
発想

1つ A円
L個 B円

##################################################### """
def check() :
    return


def main() :
    A, B, K, L = map(int, input().split())
    if B >= A*L : #別売りのほうが安い場合。
        print(A*K)
    else :
        set_buy_count = K//L
        ans = min(set_buy_count *B + K%L *A, (set_buy_count +1) *B)
        print(ans)
    return


if __name__ == "__main__" :
    main()
    #check()
