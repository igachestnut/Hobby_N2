""" #####################################################
発想

その連結成分に含まれる頂点の個数と辺の個数が等しい
UnionFind
連結成分が、親が1であるとき、その連結成分(つながっているNodeの総数)と、辺の本数が一緒である。

辺の本数と、つながっている辺の本数について調査するとよさそう
情報は親となりうる情報のみに提供することにしましょう。

find(x) →親を返す
union(x, y) → もし親が違う場合。 nodeの大きさで親決めし、Nodeを更新。また、本数親を更新し+1する。
union(x, y) → もし親が同じ場合。nodeの親のみのedgeを+=1 

self.parents(self.find(i)) == self.parents_edge(self.find(i)) :


今更ながら計算量について考察する。
(経路圧縮ありのUnionFind)
find(x)の計算量と、
union(x)の計算量
がわかると...?

- find(x)の計算量?
    - findするのが
        O(m)回?
    - unionするのが単体ではO(1)なので、全体でn回つなげる作業をするとすると、
        O(n)回?
    - 合計
        O(m+n)回?

##################################################### """
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
        self.parents = [-1] * (n)
        self.parents_edge = [0] * (n)
        
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
        if parent_x == parent_y : #もし同じ親だった場合。Node変更なし、辺の本数+=1
            self.parents_edge[parent_x] += 1
            return

        if -self.parents[parent_x] < -self.parents[parent_y] : 
            parent_x, parent_y = parent_y, parent_x #yの方がつながっているNode群が大きかった場合、要素を入れ替える。    
            
        self.parents[parent_x] += self.parents[parent_y] #結合するので要素を大きくする
        self.parents[parent_y] = parent_x #小さいほうの親Nodeを変更する
        self.parents_edge[parent_x] += self.parents_edge[parent_y] + 1 #連結小部分の変数を親に追加する。
        return
    
    
def check() :
    return


def main() :
    N, M = map(int, input().split())
    myUnion = myUnionFind(N)
    for i in range(M) :
        u,v = map(int, input().split())
        myUnion.union(u-1, v-1)

    result = "Yes"    
    for i in range(N) :
        if -myUnion.parents[myUnion.find(i)] != myUnion.parents_edge[myUnion.find(i)] :
            result = "No"
            break
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
