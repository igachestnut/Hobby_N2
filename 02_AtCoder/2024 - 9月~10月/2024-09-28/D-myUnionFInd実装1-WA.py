import sys
sys.setrecursionlimit(10**6)

def cheaker() :
    return

class UnionFind :
    def __init__(self, n) -> None:
        self.n = n
        self.parents = [-1 for i in range(n+2)] #親を記したデータ列 ※注意：有向グラフ上の親ではなく、差分を記載する親である。
        self.sabun  = [0 for i in range(n+2)] #自分の親よりどれくらい差分が生じているのかメモするデータ構造

    def find(self, x) :
        """ 現在着目中の最もな親を見つけ出す関数。
        親Nodeの位置を1~N番号で返す。また、parentとの重みを返す
        
        更に、親と子の距離が離れていた場合、現在着目している親と結合作業をする
        """
        if self.parents[x] < 0 : 
            return x, self.sabun[x] #現在の親を返す。
        else : #親が更に存在する場合
            self.parents[x], tmp_sabun = self.find(self.parents[x])
            self.sabun[x] += tmp_sabun
            return self.parents[x], self.sabun[x]
        
    def union(self, u, v, w) :
        """ x,yで与えられる二つのNodeを連結する作業
        
        場合を考える
        1. 二つとも親が存在しない場合
        2. u側に親が存在する場合 v側の親をuにし、sabun[v]をwにする
        3. v側に親が存在する場合 u側の親をvにし、sabun[u]を-wにする
        4. 両方存在し、つなげる必要がある場合。
            多いほうのNode側にくっつける。ただ、wの正負は2.と3.を参考にする
        
        """
        parent_u,t = self.find(u)
        parent_v,t = self.find(v)
        print(f"入力がu{u},v{v}, w{w}が与えられました")
        print(f"find関数より parent_u{parent_u},parent_v{parent_v}で比較します")
        print(f"現在の状況")
        print(self.parents)
        print(self.sabun)
        print("---------")
        
        # 現在着目しているNodeがもし同じ親を指している場合、つなげる必要がないため終了する
        if parent_u == parent_v : return
        
        # 親の順番を変更する
        if -self.parents[parent_u] < -self.parents[parent_v] : 
            parent_u, parent_v = parent_v, parent_u #yの方がつながっているNode群が大きかった場合、要素を入れ替える。
            w = -w
        
        self.parents[parent_u] += self.parents[parent_v]
        self.sabun[parent_v] = w + self.sabun[parent_u]
        self.parents[parent_v] = parent_u
        return
            
    def get_max_min_sabun(self) :
        """ 最大値と最小値をゲットする関数 """
        result_max, result_min = max(self.sabun), min(self.sabun)
        return result_max, result_min
        
        
def main() :
    N, M = map(int, input().split())
    myUnionFind = UnionFind(N)
        
    # データの入力開始
    for m in range(M) :
        u, v, w = map(int, input().split())
        myUnionFind.union(u, v, w)
    
    # 全ての情報を直結にする。
    for n in range(1, N+1) :
        myUnionFind.find(n)
    
    # 超過分があるかどうか確認し、答えを出力する
    rmax, rmin = myUnionFind.get_max_min_sabun()
    result = myUnionFind.sabun[1:N+1]
    if rmax > 10**18 :
        hosei = rmax - 10**18 -1 #超過した分を計算する。
        for i in range(N) : result[i] -= hosei #超過した分をマイナスする
        print(*result)
    elif rmin < -10**18 :
        hosei = rmin + 10**18 +1 #超過した分を計算する
        for i in range(N) : result[i] += hosei #超過した分をプラスする
    else : pass
    print(*result)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
