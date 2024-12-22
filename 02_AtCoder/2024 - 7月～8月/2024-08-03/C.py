""" 




"""

def cheaker() :
    return


def main() :
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    
    sum_x = 0
    tmp_sum_x = 0
    x = 0
    before_x = 0
    for i in range(N) :
        if before_x == A[i] :
            continue
        x = A[i]
        tmp_sum_x = sum_x + abs(x - before_x) * (N-i) 
        #print(f"x{x}, tmp_sum_x{tmp_sum_x}, before_x{before_x}")
        if tmp_sum_x > M :
            #行き過ぎたので一つ一つ確認して終了する。
            for j in range(before_x+1, x) :
                tmp_sum_x = sum_x + abs(j - before_x) *(N-i)
                #print(f"j{j}, tmp_sum_x{tmp_sum_x}, before_x{before_x}")
                if tmp_sum_x > M :
                    print(j-1)
                    return
            else :
                print(x-1)
                return
        else :
            before_x = x
            sum_x = tmp_sum_x
    print("infinite")
    return


if __name__ == "__main__" :
    main()
    #cheaker()
