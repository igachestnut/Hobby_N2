""" #####################################################
発想


##################################################### """
def cheaker() :
    return


def main() :
    N = int(input())
    A = list(map(int, input().split())) #A2から
    result = [0 for _ in range(N)]
    
    #逆から部下の数を加算して行く。
    for person_num in range(N, 1, -1) : #Aは2人目からN人目の情報を指している。
        #Aに代入する際は、indexに注意 
        result[A[person_num-2]-1] += result[person_num-1] + 1
    print(*result)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
