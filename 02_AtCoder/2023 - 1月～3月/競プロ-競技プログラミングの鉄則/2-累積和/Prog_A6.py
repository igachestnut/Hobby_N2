

def main() :
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))

    dist = [0 for i in range(N+1)]#リストの作り方工夫
    for i in range(1,N+1) :
        dist[i] = dist[i-1] + A[i-1]
    print(dist)
    
    for q in range(Q) :
        L,R = map(int,input().split())
        print(dist[R] - dist[L-1])
    
if __name__ == "__main__" :
    main()

def memo() :
    """
    リストの配列で、どうしても最初が一般化できないとき
    　一番最初に0などの配列を付け足して考えると良い
    リストに0を追加する。柔軟にぃ
    """
