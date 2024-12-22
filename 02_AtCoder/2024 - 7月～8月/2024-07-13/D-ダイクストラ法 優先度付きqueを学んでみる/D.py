"""  
優先度付きque 
ヒープソート? NlogNの実装をしてミル。

[参考資料](https://novnote.com/priority-queue-heapsort-impl-cpp/565/)

## MEMO - 
- Heap は塊の意味
- 常に最大もしくは最小を返すことに特化したデータ構造。
- 計算量は、挿入、取り出し両方logN

### 特性
- キューに対して要素を優先度付きで追加する
- 最も高い優先度を持つ要素をキューから取り除き、それを返す
- (オプション)最も高い優先度を持つ要素を取り除くなる参照する
- (オプション)指定した要素を取り除くことなく優先度の変更

### データ構造
- 2分ヒープ
- 完全

### 計算量
- 挿入 オーダー logN
    1. 右端に追加、
    2. ツリーの上と比較、大きいなら入れ替え()
    3. 2を繰り返し、挿入した値と比較値が 挿入<比較値になるまで継続。
- 取得 オーダー logN
    1. 一番大きい(一番小さい)を取り出す。
    2. ツリーで一番右に存在する値を一番上に挿入。
    3. 挿入値とツリーの比較。大きい要素だけを決定していく。
    
### 疑問点 pythonのヒープは、辞書型配列でも扱える?

"""

def cheaker() :
    return


def main() :
    """ グラフアルゴリズム　見えている辺orうえぃとの中で、一番軽いものを更新し続ける手法 """
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #行き先とWeightをまとめたリストを作成。
    #[[[3,2], [2,2]]] 第1Index＝現在の島 第二Index =その島から見えている辺の数 第三Index=[0]→見えている島、第三index=[1] = wight
    hen_map = [[] for n in range(N)]
    for i in range(M) :
        u, v, b = map(int, input().split())
        hen_map[u-1].append([v-1, b])
        hen_map[v-1].append([u-1, b])
    
    result_weight = [float("inf") for i in range(N)]
    result_weight[0] = 0
    
    queue = hen_map[0]
    while True :
        min_wight = float("inf")
        min_index = 0
        for que in queue :
            next_weight = que[1]+A[que[0]]
            result_weight[que[0]] = min(next_weight, result_weight[que[0]]) #行き先で最小値を見つける。
            if min_wight > next_weight :
                min_index = que[0] #次見えている位置を次の開始位置とする。
                
        queue.append(hen_map[min_index])
    
    
    
    return

class myHeapq :
    """ 自作でヒープ(キュー)を実装する
    優先度付き配列 
    最小値を返すを目的とする。
    
    コンセプト
    - 入力データ列
    [[weight, [map]], [weight, [map]], [weight, [map]],,,,]
    (かならずweight, mapの順番でデータが格納されていること。)
    - 第一引数 = 要素番号。(最大最小を挿入するだけ。)
    - 第二引数[0] = 番号
    
    注意点
    -----------
    - pythonで提供されているheapqはfunctionツールで、
    入力 method(list)でlistが変更されるという流れだが、
    今回はheapqというクラスを作成して使用することとする。
    
    Methods
    -----------
    - heapify(list) = 作成関数 @classmethod(list)
    - heapop() = 最小値取得 
    - heappush(要素) = 要素入力
    """
    def __init__(self) :
        self.heapq_obj = []
        self.heapq_len = len(self.heapq_obj)

    @classmethod
    def heapify(cls, list:list) :
        pass
    
    def heapop(self) :
        if len(self.heapq_obj) == 0 :
            raise ValueError("要素の出力ができません")
        else :
            new_head = self.heapq_obj.pop()
            result_obj = self.heapq_obj[0]
            self.heapq_obj[0] = new_head
            self._change_button_node(new_head)
            return result_obj

    def _change_button_node(self, index) :
        """ 入力indexに該当するNodeとその階下を比較して、入れ替えを行う再帰関数(出来なくなるまで入れ替え作業する。)
        
        queから要素が取り出され、新しい親がheadに持ってこられた時に実行するアルゴリズム
        
        Note
        ------
        - 何を入れ替えるのか探索
        - (必要があれば)入れ替え処理。
        
        Parameter
        ---------
        - 検査位置 : int
        """           
        button_index1 = (index+1) *2 -1 #次のNodeの位置は、番号1,2,3,,,に直した際の、2i である。 1. [0,1,2→1,2,3]  2. [次の番号取得] 3.[1,2,3,→0,1,2] 
        button_index2 = button_index1 +1

        if button_index2 < len(self.heapq_obj) :#下にNodeが両方存在
            if self._get_weight[button_index1] <= self._get_weight[button_index2] :#入れ替える優先順位の判定 左の方が最小で、左を変更するべきの場合
                if self._get_weight[button_index1] <= self._get_weight[index] :
                    self.heapq_obj[button_index1], self.heapq_obj[index] = self.heapq_obj[index], self.heapq_obj[button_index1]#入れ替え処理
                    self._change_button_node(button_index1) #次のNode探索
                elif self._get_weight[button_index2] <= self._get_weight[index] :
                    self.heapq_obj[button_index2], self.heapq_obj[index] = self.heapq_obj[index], self.heapq_obj[button_index2]#入れ替え処理
                    self._change_button_node(button_index2) #次のNode探索
            else : #優先順位2 右のほうが小さい値だった場合。
                if self._get_weight[button_index2] <= self._get_weight[index] :
                    self.heapq_obj[button_index2], self.heapq_obj[index] = self.heapq_obj[index], self.heapq_obj[button_index2]#入れ替え処理
                    self._change_button_node(button_index2) #次のNode探索
                elif self._get_weight[button_index1] <= self._get_weight[index] :                    
                    self.heapq_obj[button_index1], self.heapq_obj[index] = self.heapq_obj[index], self.heapq_obj[button_index1]#入れ替え処理
                    self._change_button_node(button_index1) #次のNode探索
        elif button_index2 >= len(self.heapq_obj) : #下にNodeが一つ存在
            if self._get_weight[button_index1] >= self._get_weight[index] :
                self.heapq_obj[button_index1], self.heapq_obj[index] = self.heapq_obj[index], self.heapq_obj[button_index1]#入れ替え処理
                self._change_button_node(button_index1) #次のNode探索
        else : #両方存在しない。
            pass
        return 
        
    def _change_top_node(self, index) :
        """ 入力indexに該当するNodeとその上階を比較して、入れ替えを行う再帰関数(出来なくなるまで入れ替え作業する。)
        
        Note
        ------
        - 上の階と比較(現在持っている情報が、上の方が上階よりも軽いならTrue)
        - (必要があれば)入れ替え処理。
        
        Parameter
        ---------
        - 検査開始位置 : int
        """           
        top_index = (index+1) *2 -1 #上階のNodeの位置は、番号1,2,3,,,に直した際の、i//2 である。 1. [0,1,2→1,2,3]  2. [次の番号取得] 3.[1,2,3,→0,1,2] 

        if 0 <= top_index :#上階が存在
            if self._get_weight[top_index] >= self._get_weight[index] :
                self.heapq_obj[top_index], self.heapq_obj[index] = self.heapq_obj[index], self.heapq_obj[top_index]#入れ替え処理
                self.self._change_top_node(top_index) #次のNode探索
        else :#上階が存在しない
            pass
        return
                        
    def _get_weight(self, index) :
        return self.heapq_obj[index][0]


if __name__ == "__main__" :
    main()
    #cheaker()
