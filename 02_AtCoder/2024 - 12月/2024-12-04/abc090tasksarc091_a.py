""" #####################################################
発想


- とりあえず、(i,j) i=2~N-1, j=2~M-1 までは必ず周りに9マス値が存在することになるので、最終的には1になる。
では、この周りについて。

##################################################### """
def check() :
    return


def main() :
    N,M = map(int, input().split())
    if N ==2 or M == 2:
        print(0)
    elif N==1 and M==1:
        print(1)
    elif N==1:
        print(max(M-2,0))
    elif M==1:
        print(max(N-2,0))
    else :
        print((N-2)*(M-2))
    return

if __name__ == "__main__" :
    main()
    #check()
