# 方針：トポロジカル順序にしたがって動的計画法（DP）による最長距離の更新を行う。
# トポロジカルソートは以下の記事の BFS algorithm に沿って行った
# 参考：https://csacademy.com/lesson/topological_sorting/

from collections import deque
import sys

# クラスを宣言
class Node:
    # コンストラクタを宣言
    def __init__(self,index):
        # メソッドを定義
        self.index = index # Node （頂点） の番号を定義
        self.parents = [] # 親 Node のリストを定義
        self.children = [] # 子 Node のリストを定義
        self.toporo = 0 # トポロジカル順序を定義
        self.memo = [] # 親 Node のリストを定義（トポロジカルソートで削除されない）
        print("classNodeの__init__処理")
        
    def __repr__(self):
        print("classNodeの__repr__処理")
        return F'Node {self.index} : toporo {self.toporo} memo {self.memo} '


def main():

    # 入力読み込み
    input = sys.stdin.readline # 入力の高速化
    N, M = map(int,input().split())

    # インスタンス（Node）を生成し、nodes に格納する。
    # ノード 0 も生成されるが使用しない。
    nodes = []
    for i in range(N + 1):
        nodes.append(Node(i))

    print(nodes)

    # 隣接 node を nears メソッドに格納する
    for _ in range(M):
        s,g = map(int,input().split()) # start, goal
        nodes[s].children.append(g)
        nodes[g].parents.append(s)
        nodes[g].memo.append(s) 

    # 探索対象 node を queue（キュー）に入れる。
    queue = deque()

    # 親 Node を持たない Node をキューに入れる。
    for node in nodes:
        if len(node.parents) == 0:
            queue.append(node)

    # トポロジカル順序を order でカウントする
    order = 1

    # queue がなくなるまで DFS を続ける。
    while queue:

        # queue の末尾から Node を 1 つ取り出す。取り出したノードについて調べる。
        # 取り出された Node は queue から消える。
        node = queue.pop()
        # print(node) # コメントアウトを外すと現在地を確認できる

        # トポロジカル順序を toporo メソッドに記入する
        nodes[node.index].toporo = order
        order += 1

        # 子 Node をメモしておく。
        children = node.children

        # 子 Node から親 Node（現在地）を削除する。
        for child in children:
            nodes[child].parents.remove(node.index)

            # 子 Node が親 Node を持たなければキューに追加する
            if len(nodes[child].parents) == 0:
                queue.append(nodes[child])

    # トポロジカル順序に Node を ソートする。Node 0 も削除しておく。
    toporo_nodes = sorted(nodes, key=lambda x: x.toporo)[:-1]

    # トポロジカル順序 i の Node まで調べたとき、その Node を通る最長経路の長さを dp[i] とする。
    # 例えば dp[3] はトポロジカル順序 3 番目の Node まで見たとき、その Node を通る最長経路の長さ

    dp = [0] * N
    for n in range(1,N):
        if len(toporo_nodes[n].memo) > 0:
            # トポロジカル順序 n 番目の Node を考える。
            # 自分の親 Node のうち、自分よりトポロジカル順序が小さな Node の中で dp が最大のものに 1 を足すと dp[n] が求まる。
            dp[n] = max([dp[j-1] for j in [nodes[i].toporo for i in toporo_nodes[n].memo]]) + 1
    print(max(dp))

# 実行の高速化
if __name__ == '__main__':
  main()
