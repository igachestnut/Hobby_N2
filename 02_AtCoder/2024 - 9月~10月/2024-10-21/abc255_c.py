""" #####################################################
発想


##################################################### """
def check() :
    print(1000000 * 1000000000000)
    return


def main() :
    X, A, D, N = map(int,input().split())
    if D < 0 : #すべての数を増える方向に調整する。
        X, A, D = -X, -A, -D
    if X <= A or D==0 : print(abs(A-X))
    elif X >= A+N*(D) : print(X-(A+N*D))
    else :
        myX = (X-A)%D #等差数列の頭からXはどの位置にいて、mod何なのか 
        print(min(myX, D-myX))
    return

def main2() :
    """ main()はWA. 項数が間違っている。 
    
    初項1, 等差3, 項数3の時の 1,4,7 で、最大数は7である。10ではない。
    """
    X, A, D, N = map(int,input().split())
    if D < 0 : #すべての数を増える方向に調整する。
        X, A, D = -X, -A, -D
    if X <= A or D==0 : print(abs(A-X))
    elif X >= A+(N-1)*D : print(X-(A+(N-1)*(D)))
    else :
        myX = (X-A)%D #等差数列の頭からXはどの位置にいて、mod何なのか 
        print(min(myX, D-myX))
    return


if __name__ == "__main__" :
    #main()
    main2()
    #check()
