""" 開始時刻(仮)

2024-09-09 - 17:27
"""

def cheaker() :
    return

class Polyomino :
    """ ミノを格納する関数
    
    MEMO
    ----------------
    - 形とひだりうえの位置を定義したいよね。
    - 基本全数調査をする。
    
    一つのブロックにおいて、おき方の全候補は最大64通り。
    0度回転 16通り * 90~270度回転 = 16*4 = 64
    全組み合わせを取得して、合致を検査すれば終了。
    ただ、ひだりうえを最も基本的な位置として行う必要がある。
    """
    def __init__(self, grid:list) :
        # みのの基底座標作成
        self._grid = []
        for i in range(len(grid)) : 
            for j in range(len(grid[0])) : 
                if grid[i][j] == "#" : self._grid.append([i+1, j+1])
        [x, y] = [min(g[0] for g in self._grid), min(g[1] for g in self._grid)]
        
        # 左上につめたみの作成
        self.grid = [[g[0]-x, g[1]-y] for g in self._grid]
        self.len_x, self.len_y = max(g[0] for g in self.grid), max(g[1] for g in self.grid)
        #print(self.grid)
        #print(self.len_x, self.len_y)
        
    def get_brock_patarn(self) -> list :
        """ 現在格納しているブロックを用いて、全ての置き方パターンを出力する関数 """
        result = []
        # 0度
        for i in range(4-self.len_x) :
            for j in range(4-self.len_y) :
                result.append([[1+i+x, 1+j+y]for x, y in self.grid])
        
        # 90度
        for j in range(4-self.len_y) :
            for i in range(4-self.len_x) :
                result.append([[1+j+y, 4-i-x] for x, y in self.grid])
        
        # 180度
        for i in range(4-self.len_x) :
            for j in range(4-self.len_y) :
                result.append([[4-i-x, 4-j-y] for x, y in self.grid])
        
        # 270度
        for j in range(4-self.len_y) :
            for i in range(4-self.len_x) :
                result.append([[4-j-y, 1+i+x] for x,y in self.grid])
        return result
    
    def get_brock_patarn_v2(self) -> list :
        """ 全ての置き方を計算する関数(解答よりvesion2) 
        
        MEMO
        ------------
        - 90 度回転した時の法則。
            (x, y) → (y, -x)にすればよいだけ。2次元平面でも同様に言えるよね。
        """
        result = []
        for i in range(4-self.len_x) :
            for j in range(4-self.len_y) :
                result.append([[   1+i+x,   1+j+y ] for x, y in self.grid])
                result.append([[   1+j+y, -(1+i+x)] for x, y in self.grid])
                result.append([[-(1+i+x), -(1+j+y)] for x, y in self.grid])
                result.append([[-(1+j+y),   1+i+x ] for x, y in self.grid])
        return result

def main() :
    A = [list(input()) for _ in range(4)]
    B = [list(input()) for _ in range(4)]
    C = [list(input()) for _ in range(4)]
    
    brock_A = Polyomino(A)
    brock_B = Polyomino(B)
    brock_C = Polyomino(C)
    
    if len(brock_A.grid) + len(brock_B.grid) + len(brock_C.grid) != 16 :
        print("No")
        return
    
    brock_A_patern = brock_A.get_brock_patarn()
    #print("A")
    #print(brock_A_patern)
    brock_B_patern = brock_B.get_brock_patarn()
    brock_C_patern = brock_C.get_brock_patarn()
    for a in brock_A_patern :
        for b in brock_B_patern :
            for c in brock_C_patern :
                grid = [ai*4 - 4 + aj for ai, aj in a] + [bi*4 - 4 + bj for bi, bj in b] + [ci*4 - 4 + cj for ci, cj in c]
                grid.sort()
                #print(grid)
                if len(grid) == 16 and grid == list(range(1, 17)) :
                    print("Yes")
                    return
    print("No")
    return


if __name__ == "__main__" :
    main()
    #cheaker()
