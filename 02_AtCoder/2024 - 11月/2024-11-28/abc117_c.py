""" #####################################################
発想

移動の最小回を見つける。
- N >= M の時、最初の時点で好きな位置に駒を置けるので、result=0
- 一回でも訪れたらOK

- flow?
    1. sort
    2. 各場所間の距離を差分で計算(M-1個)
    3. 距離のsort

##################################################### """
def check() :
    a = list(range(10))
    print(a[:-0])
    return


def main() :
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    if N >= M : 
        print(0)
        return
    X.sort()
    dis = []
    for i in range(M-1): dis.append(abs(X[i]-X[i+1]))
    dis.sort()
    if N==1: print(sum(dis))
    else: print(sum(dis[:-(N-1)]))
    return


if __name__ == "__main__" :
    main()
    #check()
