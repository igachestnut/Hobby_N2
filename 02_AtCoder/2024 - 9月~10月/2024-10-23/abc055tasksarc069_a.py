""" #####################################################
発想

N はS型のピース

Nを用いて作れる最大数
+ 
余ったピースの最大数。

min(N, c//2)


##################################################### """
def check() :
    return

def main() :
    N, M = map(int, input().split())
    result = min(N, M//2)
    amari_M = M-result*2
    if amari_M >= 2 :
        result += amari_M //4
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
