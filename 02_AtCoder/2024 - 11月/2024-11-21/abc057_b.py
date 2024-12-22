""" #####################################################
発想

- 学生がどのチェックポイント 最小距離かつ最小番号に行くか
- N,M が50 以内 
- 一人の学生がどのチェックポイントに行くのか、計算量O(M)
- それが50人


##################################################### """
def check() :
    return


def main() :
    N, M = map(int, input().split())
    students = [list(map(int, input().split())) for i in range(N)]
    check_points = [list(map(int, input().split())) for j in range(M)]
    for i in range(N) :
        result,dis = -1, float("inf")
        for j, [c,d] in enumerate(check_points) :
            tmp_dis = abs(students[i][0]-c) + abs(students[i][1]-d)
            if tmp_dis < dis :
                dis = tmp_dis
                result = j+1
        print(result)    
    return


if __name__ == "__main__" :
    main()
    #check()
