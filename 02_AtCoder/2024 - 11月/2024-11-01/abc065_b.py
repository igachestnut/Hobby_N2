""" #####################################################
発想


##################################################### """
def check() :
    return


def main() :
    N = int(input())
    A = []
    for i in range(N) : A.append(int(input()))
    
    result = 0
    before = 1 # 現在光っているボタン位置
    while result <= N and before != 2 :
        result += 1
        before = A[before-1]

    if result > N : print(-1)
    else : print(result)        
    return


if __name__ == "__main__" :
    main()
    #check()
