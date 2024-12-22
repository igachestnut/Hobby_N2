""" #####################################################
発想

- 行列で反転

  b b b 
a 0 0 0  1 0 1  0 1 0  1 1 0  0 1 1 
a 0 0 0  1 0 1  1 0 1  0 0 1  1 0 0
a 0 0 0  1 0 1  0 1 0  1 1 0  1 0 0
6,4,5 3 
1? 2?  7,8?
  b b
a 1 1
a 1 1
0, 1? 2, 3?, 4


- 偶奇で考える。
- N,M がそれぞれ偶数か奇数かで。
- N=奇数, M=奇数。
    2~min(N, M)-1 , N*M-(min(N,M)-1)~N*M-1までは無理そう
- N=偶数, M=奇数。
    上と同じっぽい??? 
- N=偶数, M=偶数
    上記の条件に追加し、どうやっても奇数個にはならない.
    これは、入れ替えることにより増える数というのが
    N,(N-1)-1, (N-2)-2,,, (N-N)-N という風に奇数を踏むことはないから。

    
...それとも愚直な全数調査をするとか。
[False]*(N*M) で構成されるリストを作る。
N,M の倍率はTrue
0はTrue
端をNで固定したとき、N-i+(M-i) はTrue

...0~N をとるi, 0~M をとるj が存在するとき、
全てのボタンを一つ一つ押したときの答えを定義していく。
ok_K = [False] *N*M
for i in range(N+1):
    for j in range(M+1):
        [i*N + j*(M-2i)] = True

##################################################### """
def check() :
    return


def main() :
    N,M,K = map(int, input().split())
    if N%2==0 and M%2==0 :
        if K%2 ==1 :
            print("No")
        elif 0<K<min(N,M) or N*M-min(N,M)<K<N*M:
            print("No")
        else :
            print("Yes")
    else :
        if 0<K<min(N,M) or N*M-min(N,M)<K<N*M:
            print("No")
        else :
            print("Yes")
    return

def main2() :
    """ 全数調査で構成可能か判定するアルゴリズム
    
    0~N のi において
    0~M のj のボタンを押したときの調査
    なので、O(N*M)で十分高速
    """
    N,M,K = map(int, input().split())
    ok_K = [False] *(N*M+1)
    #print(ok_K)
    for i in range(N+1):
        for j in range(M+1) :
            #print(i*M+j*(N-2*i))
            ok_K[i*M+j*(N-2*i)] = True
    print("Yes" if ok_K[K] else "No")
    return

if __name__ == "__main__" :
    main2()
    #check()
