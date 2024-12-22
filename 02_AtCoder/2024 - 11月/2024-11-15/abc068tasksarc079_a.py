""" #####################################################
発想

1→N が可能か
2つしか使ってはいけない。
つまり、片方に 1,Nのどっちかが存在しないと達成不可能。

そこで, 2~N-1 の配列を作り、
1,Nが出てきたら、残りの数字を配列に加算。
2になったら可能、それ以外は不可能
という形にする。
##################################################### """
def check() :
    return


def main() :
    N, M = map(int, input().split())
    check_point = [0 for i in range(N-2)]
    for m in range(M) :
        a, b = map(int, input().split())
        if a == 1 or a==N :
            check_point[b-2] += 1
            if check_point[b-2] >= 2:
                print("POSSIBLE")
                return
        elif b == 2 or b == N :
            check_point[a-2] += 1
            if check_point[a-2] >= 2 :
                print("POSSIBLE")
                return
    else :
        print("IMPOSSIBLE")
    return


if __name__ == "__main__" :
    main()
    #check()
