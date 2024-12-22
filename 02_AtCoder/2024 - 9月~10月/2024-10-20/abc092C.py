""" #####################################################
発想

MEMO
- 0始動 0終点
- 基本は番号順に訪れる
- i 番目だけ訪れるのをやめた。
- 旅行にかかるお金の総和


##################################################### """
def check() :
    return


def main() :
    N = int(input())
    A = [0] + list(map(int, input().split())) + [0]
    sum_a = 0
    for i in range(1, N+2) :
        sum_a += abs(A[i] - A[i-1])
    
    for i in range(N) :
        # now = i, nex=i+1, nexnex=i+2
        if A[i] < A[i+2] :#スキップ時、大きくなっている場合
            if A[i] <= A[i+1] <= A[i+2] :#順当に大きくなる。
                print(sum_a)
            elif A[i] > A[i+1] :
                print(sum_a - (A[i]-A[i+1])*2)
            else :
                print(sum_a - abs(A[i+1]-A[i+2])*2) #差の絶対値×2だけ減らす
        elif A[i] > A[i+2]: #スキップ時、小さい方向に移行しようとしている
            if A[i] >= A[i+1] >= A[i+2] :#順当に小さい方向へ移行
                print(sum_a)
            elif A[i] < A[i+1] :
                print(sum_a - (A[i+1]-A[i])*2)
            else :
                print(sum_a - abs(A[i+2]-A[i+1])*2)
        else :#2つ先の到達地点が移動する必要ない場合
            print(sum_a - abs(A[i+1]-A[i+2])*2) #差の絶対値×2倍だけ移動が削減できる
    return

def main2() :
    """ 詳細な条件分岐でなくても求める方法はあったのか考察したいスペース 
    
    考察メモより
    ac - (ab + bc)
    """
    N = int(input())
    A = [0] + list(map(int, input().split())) + [0]
    sum_a = 0
    for i in range(1, N+2) : sum_a += abs(A[i] - A[i-1])
    
    for i in range(N) :
        ab, bc, ac = abs(A[i]-A[i+1]), abs(A[i+1]-A[i+2]), abs(A[i+2]-A[i])
        print(sum_a - abs(ac -(ab +bc)))
    return    

if __name__ == "__main__" :
    main2()
    #check()
