""" #####################################################
発想

N = 国 10**6
M = 道路
双方向に行き来可能

選手を本選会場に集める際にかかる通行料金の和を最小化したい
K = 本線を開催する都市の個数

今回の問題は、
複数人で通っても、通行料金は1人通った時と一緒であるということ。
最短経路を知りたい！ という要件と、
最も効率的に集まるにはどうしたらいいのか?
という話である。
a-b-c がある。
 2 4
aとbの人間がcに集まりたい気にかかるお金→2+4=6
aとcの人間がbに→2+4
           aに→2+4
つまり、どこが開催位置でも、
答えは1意に定まっている。

では、複数開催位置がある場合?
...多分、作成された最小全域木において、最も大きい重みのedgeを使用しないように
つまり、w_max が 2→3の時、2,3に会場を置く的な感じになるとよさそう。

余談だが計算量について
dequeの作成
Mlog(M)
+
UnionFind 
- find = O(1)
- union = O(1)
- unionを最大M回繰り返す
MlogM + M

##################################################### """
import heapq

class myUnionFind :
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
    """
    def __init__(self, n) :
        self.n = n
        self.parents = [-1] * n 
        self.W = [] #グラフ構成に使用されているEdgeの重み
        
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

    def union(self, x, y, w) :
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

        if parent_x == parent_y : return
        
        if -self.parents[parent_x] < -self.parents[parent_y] : 
            parent_x, parent_y = parent_y, parent_x #yの方がつながっているNode群が大きかった場合、要素を入れ替える。    
            
        self.parents[parent_x] += self.parents[parent_y] #結合するので要素を大きくする
        self.parents[parent_y] = parent_x #小さいほうの親Nodeを変更する
        self.W.append(w)
        return

    def get_total_price(self, k) :
        """ すべての参加者が払う費用の合計を計算する """
        return sum(self.W[:-(k-1)]) if k>1 else sum(self.W)
  

def check() :
    return


def main() :
    """ クラスカル法を用いて最小全域木の実装を目指す

    クラスカル法とは?(貪欲法の1種)
    Edge集合E の小さい重い順に調査する。
    取り出し方法としてはheapqを用いる。
    データ構造にはUnionFindを用いる    
    """
    N, M, K = map(int, input().split())
    myTree = myUnionFind(N)
    deque = []
    for i in range(M) :
        u,v,w = map(int, input().split())
        deque.append([w, [u-1, v-1]])
    heapq.heapify(deque)

    for i in range(M) :
        que = heapq.heappop(deque)
        myTree.union(x=que[1][0], y=que[1][1], w=que[0])
    
    result = myTree.get_total_price(K)
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
