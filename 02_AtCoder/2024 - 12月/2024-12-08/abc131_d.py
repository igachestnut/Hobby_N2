""" #####################################################
発想


- 締め切りの順番順に仕事を繰り返した結果、
終わるか終わらないか判定する。

i index i秒までにおける仕事の総和(累積?)
- 制約B が10**9 なので間に合わない・

 0, 1, 2, 3, 4
[]

##################################################### """
def check() :
    return

import heapq
def main() :
    N = int(input())
    query = []
    for i in range(N) :
        a,b = map(int, input().split())
        query.append([b, a])
    heapq.heapify(query)

    result = "Yes"
    tmp_worktime = 0
    for i in range(N) :
        [b,a] = heapq.heappop(query)
        tmp_worktime += a
        if tmp_worktime > b :
            result = "No"
            break
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
