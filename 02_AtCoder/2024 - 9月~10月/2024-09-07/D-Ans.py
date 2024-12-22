# D6の引用

import sys
sys.setrecursionlimit(2000)  # 再帰の深さの制限を2000に設定

class UnionFind :
    def __init__(self, n) :
        self.n = n
        self.parents = [-1] * (n+2)
        self.is_wall = [-1] + [1] * n + [-1]
        self.L = list(range(n+2))
        self.R = list(range(n+2))
        
    def find(self, x) :
        if self.parents[x] < 0 : return x #0未満 (親が存在しない場合、入力値xは全ての親であるということ)
        else : #親が更に存在する場合
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y) :
        parent_x = self.find(x)
        parent_y = self.find(y)
        
        if self.parents[parent_x] > self.parents[parent_y] : #yの方がつながっているNode群が大きかった場合 (-1) と (-2) この場合より小さいときとなる。
            x, y = y, x #要素を入れ替える。
        
        self.parents[parent_x] += self.parents[parent_y] #結合するので要素を大きくする
        self.L[parent_x] = min(self.L[parent_x], self.L[parent_y]) #2つのNodeを結合したため、最小位置を返す。
        self.R[parent_x] = max(self.R[parent_x], self.R[parent_y]) #2つのNodeを結合したため、最大位置を返す
        self.parents[parent_y] = parent_x #小さいほうの親Nodeを変更する
        return
    
    def get_break_points(self, x) :
        x = self.find(x) #現在着目しようとしている親情報の取得
        if self.is_wall[x] == 1 : return [x] #現在位置を出力して終了
        
        results = [] #位置を格納する変数
        # 左に調査
        while self.is_wall[self.L[x]] != -1 : #端に到達したら終了
            if self.is_wall[self.L[x]-1] == 1 : #現在着目中のNodeの左に未破壊のオブジェクトが存在している場合
                results.append(self.L[x]-1) #破壊する位置を出力して右へ移動
                break
            else : #行き先は破壊する位置ではないが、既存のNodeが存在する場合。
                self.union(x, self.L[x]-1) #現在値xと、L-1のparentをつなげ、親parent値の更新。
                x = self.find(x) #現在着目しているxは親ではない可能性があるため、更新する。
        
        # 右に調査
        while self.is_wall[self.R[x]] != -1 : #右端に到達したら終了
            if self.is_wall[self.R[x]+1] == 1 : #右に未破壊のオブジェクトが存在する場合
                results.append(self.R[x]+1)
                break
            else :
                self.union(x, self.R[x]+1)
                x = self.find(x)
        
        return results
    
    def break_wall(self, x) :
        """ 入力された位置を破壊し、左右のNodeとつなげる作業をする関数 """
        if self.is_wall[x] == 0 : return #破壊済みはスルーする。
        self.is_wall[x] = 0 #壁破壊
        
        # 左側空き調査            
        if self.is_wall[x-1] == 1 or self.is_wall[x-1] == -1 : pass #未破壊 or 左端の場合
        else : #破壊済みのオブジェがある場合
            self.union(x, x-1)
        
        # 右側空き調査
        if self.is_wall[x+1] == 1 or self.is_wall[x+1] == -1 : pass #未破壊 or 右端の場合
        else :
            self.union(x, x+1)
        return        
    
    def get_wall_count(self) :
        """ このUnionFindにおける、壁の残り数を取得する関数 """
        return sum(iw == 1 for iw in self.is_wall)

def main() :
    H, W, Q = map(int, input().split())
    col_wall_map = [None] + [UnionFind(W) for i in range(H)] + [None] #1~Wであることに注意 
    row_wall_map = [None] + [UnionFind(H) for j in range(W)] + [None]

    for q in range(Q) :
        R, C = map(int, input().split()) #R=たてにおける行数の位置, C=横の何要素目か 
        
        #破壊位置の全検出
        destruction_points = [] #壁破壊する位置の格納先
        tmp_j = col_wall_map[R].get_break_points(C) #水平方向における破壊場所の調査
        for j in tmp_j : destruction_points.append([R, j]) #存在するだけ破壊位置の追加
        tmp_i = row_wall_map[C].get_break_points(R) #垂直方向
        for i in tmp_i : destruction_points.append([i, C])
        
        #全ての破壊位置について、Node作成と調査実行!
        for [i, j] in destruction_points :
            #print(f"破壊位置i:{i}, j:{j}")
            col_wall_map[i].break_wall(j) #水平方向破壊処理
            row_wall_map[j].break_wall(i) #垂直方向破壊処理
    
    result = 0
    for i in range(1, H+1) :
        result += col_wall_map[i].get_wall_count() 
    print(result)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
