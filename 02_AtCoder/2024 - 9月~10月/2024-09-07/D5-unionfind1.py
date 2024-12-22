""" #####################################################
発想

UnionFindで実装してみる

- 注意点
    - Union by side を利用する。親位置だけでなく、結合数も保持し、大きい頂点数の親に結合していく方針。→計算量(O (logN))まで削減される
    
--------
- さて、どのように実装するのだろうか。
    - 今回重要になってくるのが、壁の位置からではなく、破壊位置に着目すること。
    - 水平のつながり、垂直のつながりを各行列で把握すること
    
- 重要なのが破壊位置と、破壊場所の親位置を把握すること。
- このDB構造において、垂直と水平は「全くの別物」と考えた方が良いだろう。
- 必要な情報はシンプル
    1. 破壊したい位置はどこ?
    2. 破壊したい位置+-1した場所に壁は存在する?もしくは、壁はない?
        1. もしすでにくりぬかれている場合
            →そこの親は0以上の数値である。
            自身と見つけたいNodeを結合する。
            その上で、結合した上で+1はくりぬかれているか再確認する。(上階の2をやり直す。)
        2. mapの外の場合
            →そこの親は存在しない None?
            →処理を終了する。
            この定義が難しい。
            逆に mapの最外端である場合と考えたほうがよさそう。→L=0, R=n-1 だった場合
            すると、これ以上進めないので処理を終了する。
        3. 壁の場合
            →そこの親は-1である。 unionする。
    
    
    
- どうやって破壊位置を検出する？
    というか
    1. 破壊位置の全検出 
    2. 残っている破壊位置とUnionFindを適用する。以上で良くない?
    
    破壊位置で重要なのが、
    その破壊位置を実施した際、上下左右につながりは存在するのかを検知する必要があるということ。
    
    2. の追記
        破壊位置が分かれば後どんな状態でもつなげればよいだけ。
        そのNodeの上下でつなげる作業をする。
        
    
    
    
    
殴り書き
------------------    
- 津田君に質問
    - UnionFind木とばご存じですか?
    UnionFindとは、各Nodeにおける親を格納するデータ構造です。
    詳しくはUnionFind の記事を見て下さい。
    
    今回私は、この親を更新するための最悪計算量について考えていました。
    適当な実装方法とは別に、
    親の更新における、処理回数を抑える方法として、「Union by side」があるらしいです。
    これを用いてUnionFindを作成すると 親Nodeを更新するのに必要な最悪計算量が logNで済むとのことでした。

    親を1度定義した後、全ての親が変更されることによって生じる
    、、、、、、、、、、
    途中でやめます。竹田海渡は頭の中でだんだん整理ができてきたからです。
    
    

##################################################### """

class UnionFind :
    """ 1行分のUnionFindデータ構造
    
    以下の識別番号は全て1~Nで入力すること。
    
    Parameters
    --------------
    - n : int
        Node列の長さ. 実際のNodeは左端0 と右端 n+1を含む構造となる。
    
    Functions
    -------------------
    
    MEMO
    ----------
    - このデータ構造はUnionFindと呼ばれるデータ構造である。
    - 1次元配列 のつながり状況を保持するもの。
    - 最初のすべての親は -1 で存在しないこととなっている。
    - また、-1 の中で - の負の部分は これ以上親が存在しないという意味であり、数字の部分は子Nodeのつながっている要素数を表す。
        例として、 1-2-3 がつながっており、全ての親が2であるとき、parentsは
        # paretns  [1, -3, 1] このようになる。
        すると、入力で与えられる任意位置のNodeがつながっている数を知りたい時、
        x = 0 (0要素目のつながっている要素数を算出してね。という入力)
        自身が全ての親でない為、親Nodeを参照 parent_node = self.find[x]
        全ての親において、要素数を返す。return -self.parents[parent_node]
        
    - 主な機能 2選
        1. find(x) : 入力値x(Node名x)の位置における、全ての親を返す関数
        2. union(x, y) : 入力値x, y を結合する。
            具体的には、x,y のそれぞれのNode群における、全ての親u, v を、サイズが大きいほうの全ての親側に結合する。
            
    - この問題において、必要な関数
        1. union_and_break(x) : 入力値x の位置を調査し、parent = -1 となっている左右のNodeを見つけ出し結合する。
        
    """
    def __init__(self, n) :
        self.n = n
        self.parents = [-1] * (n+2)
        self.is_wall = [-1] + [1] * n + [-1]
        self.L = list(range(n+2))
        self.R = list(range(n+2))
        
    def find(self, x) :
        """ x が所属する「全ての親」を見つける関数。
        
        併せて、次からO(2)で実装できるように 現時点の着目親情報を更新してくれる。
        
        MEMO 
        -----------
        - この関数は再帰関数である。
            - もし現在着目しているNode (x) がすべての親だった場合、要件を達成したため、xを返す。
            - これが親ではない。上階にNodeが存在する場合、
                1. 現在のすべての親を 全ての親となるであろうとして、find(x)を使用し、parentを見つけ出す。
                2. 見つけ出したparentを現在の新規な親として設定する。
                3. 設定した新規parentは全ての親であるため、要件を達成した。parents[x]全ての親を返す。
                
        - 計算量について
            - 全ての親を返すまでの処理数を書き起こす。
                1. 親を調べ、
                2. 親にたどり着き、
                3. その親をたどってきたすべてのNodeに適用する
                という行ったり来たりしているようでめっちゃ大きい計算量になりそうだが、
                1度辿ってしまえば、1~2でたどった全ての経路を圧縮することができる。(つまり再度調べなくてよい)
                UnionFindの1次元構造でlenがn個であることを考えると、計算量は O(N)? ※もし全てのNodeをつなげる場合。完成したら、どのNodeからfindしても 親Nodeの検索→これ以上親Nodeは存在しない というO(2)になる。                
            - 全ての親が書き変わった時の計算量は???
                - 例として、
                    [1, -3, 1, -1, -1]から、4番目の要素を全ての親にしましょう!と変更した場合、
                    [1, 3, 1, -4, -1]このような変更が見られる。
                    すると次にx=0, x=2を参照すると全ての値更新が必要になるのではないか?という問題。
                - 結論 : 上記で述べた例では計算量が肥大化してしまう。
                - ではどうするのか? → Union by side という考え方を使う。
                - Union by side とは? → Nodeを結合する際、要素の多いほうを全ての親にしましょう!というもの。(詳しくはunionのMEMOにて)
        """
        if self.parents[x] < 0 : return x #0未満 (親が存在しない場合、入力値xは全ての親であるということ)
        else : #親が更に存在する場合
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y) :
        """ 任意の要素x, y の親Nodeを合併する関数 
        
        MEMO
        -----------
        - Flow (Union by side を用いた結合方法)  - O (logN)になる
            1. x, y のそれぞれの全ての親を見つける。
            2. x, y のすべての親のうち要素が大きいほうを調査する。(要素が大きいほう(親になるものをxにする))
            3. x 側に y側を合併する。
        
        - 計算量について。
            - なぜ要素の多いほうに結合すると計算量が抑えられるの?
                関数find にて、「全ての親が変更されると下のそれに属するすべてのNodeも全ての親を変更しなければならない」ということにより、変更する量が多すぎるのではないか?という懸念が生じた。
                この変更しなければならない量について考える。
                まず、与えられた1次元配列において結合する(Union)処理は、N回以下しか実行しない。N以上実施しても、既に親Nodeが一緒である.(全ての親の更新は 1度決まったら戻ることは無い。)
                仮にN回のUnionFind で全ての親が書き換えられる量というのは、つなげようとするx, yのNodeの小さい量である。
                従って、x, yのつながっているNode群(ここでは仮に xn, yn (xの全つながり数, yの全つながり数)) のうち、変更しなければならないのは必ず min(xn, yn)回である。
                よって、更新しなければならない処理数(最悪計算量)は 常に全体の半分である。
                ...みたいな感じ。
                証明っぽく書いたつもりだが、なんとなく数理の証明とは違うってことだけは分かる。ただ、具体的にどこが違うのか、どう書きなおせばよいのかが分からない。キレそう
        """
        parent_x = self.find(x)
        parent_y = self.find(y)
        
        if -self.parents[parent_x] < -self.parents[parent_y] : 
            parent_x, parent_y = parent_y, parent_x #yの方がつながっているNode群が大きかった場合、要素を入れ替える。    
            
        self.parents[parent_x] += self.parents[parent_y] #結合するので要素を大きくする
        self.L[parent_x] = min(self.L[parent_x], self.L[parent_y]) #2つのNodeを結合したため、最小位置を返す。
        self.R[parent_y] = max(self.R[parent_x], self.R[parent_y]) #2つのNodeを結合したため、最大位置を返す
        self.parents[parent_y] = parent_x #小さいほうの親Nodeを変更する
        return
    
    def get_break_points(self, x) :
        """ 入力値xより左右に調査し、破壊場所を特定し出力する関数 
        
        Returns
        ----------
        - list 
            破壊するべきx位置を格納したリストを返す。
        
        MEMO
        ---------------
        - 左右に破壊しなければならないことが前提である。(parents[x] == -1)なら現在位置を出力して終了。
        - 処理をシンプルにするため、右と左の調査はそれぞれ別々行う。
        - 注意 : 調査位置が空きだったが、左右に空きがあるが親が違う場合が存在する。そのため、破壊位置を見つけるまでの過程に、結合処理と全ての親を更新する処理を挟む
        
        - 高速化のエッセンが詰まっているコード。
            破壊位置の特定に、L, Rを使用しているのがマグマなんです。
        """
        x = self.find(x) #現在着目しようとしている親情報の取得
        if self.parents[x] == -1 : return [x] #現在位置を出力して終了
        
        results = [] #位置を格納する変数
        # 左に調査
        while self.L[x] > 1 : #端に到達したら終了
            if self.parents[self.L[x]-1] == -1 : 
                results.append(self.L[x]-1) #破壊する位置を出力して右へ移動
                break
            else : #行き先は破壊する位置ではないが、既存のNodeが存在する場合。
                self.union(x, self.L[x]-1) #現在値xと、L-1のparentをつなげ、親parent値の更新。
                x = self.find(x) #現在着目しているxは親ではない可能性があるため、更新する。
        
        # 右に調査
        while self.R[x] >= self.n : #最大右に到達したら終了
            if self.parents[self.R[x]+1] == -1 :
                results.append(self.R[x]+1)
                break
            else :
                self.union(x, self.R[x]+1)
                x = self.find(x)
        
        return results
    
    def break_wall(self, x) :
        """ 入力された位置を破壊し、左右のNodeとつなげる作業をする関数 """
        self.is_wall[x] = 0 #壁破壊
        
        # 左側空き調査            
        if self.is_wall[x-1] == 0 or self.is_wall[x-1] == -1 : pass #未破壊 or 左端の場合
        else : #破壊済みのオブジェがある場合
            self.union(x, x-1)
        
        # 右側空き調査
        if self.is_wall[x+1] == 0 or self.is_wall[x+1] == -1 : pass #未破壊 or 右端の場合
        else :
            self.union(x, x+1)
            
        return        
    
    def get_wall_count(self) :
        """ このUnionFindにおける、壁の残り数を取得する関数 """
        return sum(iw == 1 for iw in self.is_wall)

def cheaker() :
    A = [1, 1, 0, 0]
    result = sum(a == 1 for a in A)
    return


def main() :
    """ mainflow
    
    Desctiption
    ----------------
    - flow
        1. 破壊位置の全検出 
            - 該当位置のparents = -1 か？
            - 該当場所の水平方向において破壊する位置は?
            - 該当位置の上下で初めて -1となる場所は?
             
        2. 破壊位置それぞれにNodeをつなげる作業を行う。
    """
    H, W, Q = map(int, input().split())
    col_wall_map = [None] + [UnionFind(W) for i in range(H)] + [None] #1~Wであることに注意 
    row_wall_map = [None] + [UnionFind(H) for j in range(W)] + [None]

    for q in range(Q) :
        R, C = map(int, input().split()) #R=たてにおける行数の位置, C=横の何要素目か 
        
        #破壊位置の全検出
        destruction_points = set() #壁破壊する位置の格納先
        tmp_j = col_wall_map[R].get_break_points(C) #水平方向における破壊場所の調査
        for j in tmp_j : destruction_points.add(R*(W+2) + j+1) #存在するだけ破壊位置の追加
        tmp_i = row_wall_map[C].get_break_points(R) #垂直方向
        for i in tmp_i : destruction_points.add(i*(W+2) + C+1)
        
        #全ての破壊位置について、Node作成と調査実行!
        for index in destruction_points :
            i, j = index // (W+2), index % (W+2) -1
            col_wall_map[i].break_wall(j) #水平方向破壊処理
            row_wall_map[j].break_wall(i) #垂直方向破壊処理
    
    result = 0
    for i in range(1, H+1) :
        result += col_wall_map[i].get_wall_count() 
    print(result)
    
    print("---------------------")
    for i in range(1, H+1) :
        print(col_wall_map[i].parents)
    print("------------------------")
    for j in range(1, W+1) :
        print(row_wall_map[j].parents)
    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
