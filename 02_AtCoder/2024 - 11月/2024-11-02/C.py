def check() :
    return

from collections import defaultdict
def main() :
    N = int(input())
    A = list(map(int, input().split()))
    
    d = defaultdict(int) #value:index を格納する辞書。index=0の時、初検知である
    B = []
    for i in range(N) :
        # 現れた要素のindexを確認する
        b = d[A[i]]
        if b == 0 :
            B.append(-1)
        else :
            B.append(b)
        d[A[i]] = i+1 #要素の位置を更新する

    print(*B)
    return


if __name__ == "__main__" :
    main()
    #check()
