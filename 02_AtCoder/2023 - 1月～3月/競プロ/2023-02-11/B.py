def cheaker() :
    return

class UnionFind() :
    def __init__(self,n) :
        #親のつながりをメモするリスト
        #数である。
        self.par = list(range(n+1))
        self.n = n#len

    #その要素のおおもとの親を探す関数
    def find(self,x) :
        if self.par[x] == x :
            #その要素が親であるためindexを返す
            return x

        #親がその番号に格納されている場合
        else :
            return self.par[x]

    #与えられた二つの要素は連結成分か査定する
    def union(self,X) :
        x = self.find(X)
        y = self.find(X+1)
        #親が同じだった場合、小さい側の奴に連結する
        if x == y :
            pass

        #親が違う場合、大きいほうの数字を全て小さくする
        if x < y :
            for i in range(1,self.n+1) :
                if self.par[i] == y :
                    self.par[i] = x

def main() :
    N,M = map(int,input().split())
    a = list(map(int,input().split()))
    uf = UnionFind(N)
    for i in range(M) :
        uf.union(a[i])
        
    G = uf.par[1:]
    que = []
    ans = []
    GMax = max(G)+1
    i = 0
    while i < len(G) :
        Min = min(G)
        while i < len(G) and G[i] == Min :
            que.append(i+1)
            G[i] = GMax
            i += 1
        que.reverse()
        for k in range(len(que)) :
            ans.append(que[k])
        que = []
    print(*ans)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
