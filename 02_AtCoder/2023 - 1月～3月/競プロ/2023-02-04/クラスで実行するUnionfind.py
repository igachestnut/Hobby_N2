
def MEMO() :
    """
    クラスで実行するUnionfind
    （グラフ（木）を作ってみよう！）
    作り方と構造

    https://qiita.com/white1107/items/52fd4149bb1846862e38

    Union　⇒グループづくり
    find ⇒グループに属しているかどうか

    高速化のtip1
    　縦につなげると時間がかかる
    　⇒親に直接繋げるイメージ
　　
　　高速化のtip2
      木の高さを保持して置き、低い方を高いほうにつなげる
      （経路圧縮の計算量を減らす）

    parents(親)
    par = [i for i in range(N+1)]
    最初はつながっていないので、親は各頂点になる。

    自分の親を見つける⇒find
    要素x,yが同じグループかどうかを確認する方法same

    自分が親の時
    　⇒自分の数を返す
    それ以外の時
    　⇒findを実行、親を探す
    def find(x):
        if par[x] == x:
            return x
        else:
            par[x] = find(par[x]) #経路圧縮
            return par[x]
    お互いの親が一緒であるかどうか（同じグループかどうか）の査定
    def same(x,y) ;
        return find(x) == find(y)

    unite
    それぞれの親を確認して異なる場合のみ親を統一
    def unite(x,y) :
        x = find(x)
        y = find(y)
        if x == y :
            return 0
        else :
            par[x] = y
        
    #2023-2-5意味わからん
    結局何が作りたいのか感覚的に理解できない
    どうなったらいいの？
    何を作りたいの？何を判定したいの？



parents
各要素の親要素の番号を格納するリスト
要素が根（ルート）の場合は-(そのグループの要素数)を格納する

find(x)
要素xが属するグループの根を返す

union(x, y)
要素xが属するグループと要素yが属するグループとを併合する

size(x)
要素xが属するグループのサイズ（要素数）を返す

same(x, y)
要素x, yが同じグループに属するかどうかを返す

members(x)
要素xが属するグループに属する要素をリストで返す
関連記事: Pythonリスト内包表記の使い方
その後に行う処理によっては集合内包表記やジェネレータ式を使うほうが効率的かもしれない（下のroots()も同じ）

roots()
すべての根の要素をリストで返す

group_count()
グループの数を返す

all_group_members
{ルート要素: [そのグループに含まれる要素のリスト], ...}のdefaultdictを返す

defaultdictは辞書dictのサブクラス

collections - defaultdict --- コンテナデータ型 — Python 3.9.0 ドキュメント

__str__()
print()での表示用
ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
f文字列を利用している

    
    """

N = 6
par = [i for i in range(N+1)]
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x]) #経路圧縮
        return par[x]
def same(x,y):
    return find(x) == find(y)
def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    par[x] = y

for i in range(5) :
    x,y = map(int,input().split())
    print(par)
    unite(x,y)
    print(par)
