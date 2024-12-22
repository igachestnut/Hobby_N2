from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):#要素xが属するグループの根を返す
        if self.parents[x] < 0 :#もしそれが親判定ならその数（親）を返す。
            return x
        else:#見た数が親ではない（親がいる）場合、その数の先で親を見つける
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):#二つの要素を併合する
        #まず、見ている要素の親を見つける
        x = self.find(x)
        y = self.find(y)

        #親が一致している場合、parを変えずに終了
        if x == y:
            return

        #もし親が
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        #親が一致していない⇒親要素の統合と、最初の要素だけ
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

def main() :
    N,M = map(int,input().split())
    #A = list(map(int,input().split()))
    G = [list(map(int,input().split())) for _ in range(M)]
    print(G)
    uf = UnionFind(N)
    print(uf.parents,"最初parents")
    for m in range(M) :
        uf.union(G[m][0],G[m][1])
        print(uf.parents,"{}回目の入力".format(m))

    """
    10 5
    1 2
    3 4
    5 6
    1 3
    1 5

    出力例
    [[1, 2], [3, 4], [5, 6], [1, 3], [1, 5]]
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1] 最初parents
    [-1, -2, 1, -1, -1, -1, -1, -1, -1, -1] 0回目の入力
    [-1, -2, 1, -2, 3, -1, -1, -1, -1, -1] 1回目の入力
    [-1, -2, 1, -2, 3, -2, 5, -1, -1, -1] 2回目の入力
    [-1, -4, 1, 1, 3, -2, 5, -1, -1, -1] 3回目の入力
    [-1, -6, 1, 1, 3, 1, 5, -1, -1, -1] 4回目の入力

    -1< par[x]ならそれが親を示し、その要素数を示す。
    1以上なら内蔵されている数が自身のつながり（親）を示す

    10 5
    5 1
    3 1
    3 4
    6 5
    2 1
    [[5, 1], [3, 1], [3, 4], [6, 5], [2, 1]]
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1] 最初parents
    [-1, 5, -1, -1, -1, -2, -1, -1, -1, -1] 0回目の入力
    [-1, 5, -1, 5, -1, -3, -1, -1, -1, -1] 1回目の入力
    [-1, 5, -1, 5, 5, -4, -1, -1, -1, -1] 2回目の入力
    [-1, 5, -1, 5, 5, -5, 5, -1, -1, -1] 3回目の入力
    [-1, 5, 5, 5, 5, -6, 5, -1, -1, -1] 4回目の入力

    """ 
    return


if __name__ == "__main__" :
    main()



