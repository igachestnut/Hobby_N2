""" #####################################################
発想


##################################################### """
def check() :
    return


def main() :
    N = int(input())
    A = list(map(int, input().split()))

    late = [0] * 8 #各レートに人は存在するか記載。レッドコーダーまで
    r_extra = 0 #レート3200以上の方の人数
    for i in range(N) :
        if A[i] >= 3200 :
            r_extra += 1
        else :
            late[A[i]//400] = 1
    print(max(1, sum(late)), sum(late)+r_extra)
    return

if __name__ == "__main__" :
    main()
    #check()
