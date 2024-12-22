""" #####################################################
発想

- 数え上げ。
- 全数
    - R,G,を固定して、残りのBを定義、→行けるかを全通り実施する。

##################################################### """
def check() :
    print(0%2)
    return


def main() :
    """ R,Gを固定して数え上げる
    
    r,gは、箱Rをi,j個購入したときのボールの総数
    """
    R,G,B,N = map(int, input().split())
    result = 0
    for r in range(0,N+1,R) :
        for g in range(0, N+1-r, G) :
            if (N-r-g)%B == 0 :
                #print(r,g)
                result += 1
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
