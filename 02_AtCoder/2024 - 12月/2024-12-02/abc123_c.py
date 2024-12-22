""" #####################################################
発想

- 全員都市6に到着するまでの時間
- 仮に、全員都市2に移動するまでに要する時間。
    A=2, N=20の時、
    ans =10 (2*10)回繰り返す。
- 仮に、全員が都市3に移動するまでの時間。もし、人数が2人ずつ増えたとき
    B=3, N=20で、最初は0, 以降2人ずつ増えていく。
    ある時間tの時送ることができる人の数=bとすると、
    t 1 2 3 4 5
    b 0 2 2 2 2,,,
    min(A,B) だけ送ることができる。
    開始位置は、Node1から初めて人が到着したとき。

- A,B,C,D,E >0 である限り、必ずNode5におけるtの開始時間t=4である。
- 今回全員移動しきることが目標である。
    - エスパーポイントだが、ある地点に何人いるのかは関係ない。
    - Node5において、N//min(A,B,C,D,E) + 1 if N%min(A,B,C,D,E)!=0 else 0
    である。
##################################################### """
def check() :
    return


def main() :
    N = int(input())
    min_passengers = min([int(input()) for i in range(5)])
    result = 4+ N//min_passengers
    result += 0 if N%min_passengers==0 else 1
    print(result)
    return

def main2() :
    """ 切り上げテク """
    N = int(input())
    min_passengers = min([int(input()) for i in range(5)])
    result = 4+ (N + min_passengers-1)//min_passengers
    print(result)

if __name__ == "__main__" :
    main()
    #check()
