""" #####################################################
発想

- https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cs

- SとTを一致させることができる???
- 任意回できる処理
    - 削除
    - 一つの文字を別のものに変更する
    - Sの中を適当な位置に、文字を一つ挿入

- Tを目指す。 
- Sの任意要素si, Tの任意要素i (0<i<=min(len(T),len(S)) 
- case 1: si == ti の場合
    変える必要がない。???
    - S=bbttb, T=attaa の場合?? 同じ位置はi=3である。けど前を1つ削除するとよさそう?
    - いやいや、bbttb i=2を削除して bttb, 末尾に追加してbttba すると合計2
    - S=ababab, T=bababt の場合、i=1を削除してbabab,末尾に追加すると最速bababt
    - 削除してスライドさせることが重要???
    - 最も一致している部分文字列を見つけ出して、

.....編集距離 動的計画法を使用するとよい
- [編集距離]
    - 文字列sから文字列tへ変換するために必要な処理回数
    - 置換、削除、挿入など自由にできる
- [レーベンシュタイン距離]
    - 編集距離を算出する条件が、挿入、削除、置換だけ

記事
- https://yapatta.hatenablog.com/entry/2018/12/22/143317
にて、レーベンシュタイン距離の導出方法が解説してある。
レーベンシュタイン距離 LP(S,T) を考える
- 以下の漸化式を用いて考える.
1. もし |S| == 0 or |T| == 0の時、
LP(S,T) == max(|S|, |T|) になるね
2. もし S = desk, T= book の時
LP(S,T) = LP(desk, book) = LP(des, book)
最後尾の情報が一致していた時、除外して考えても答えは一緒
3. 削除するとき
LP(des, boo) = LP(de, boo) +1
des から sを削除したときものは deとなる。編集回数は1回なので
LP(de, boo) +1 でよい。
4. 挿入について
LP(des, boo) = LP(des, bo) +1
これは、Sに末尾Oを追加したとき(LP(deso, boo) +1 )編集距離は1回となることを表現し、
1の性質を用いて整理したらこうなる。
5. 置換について
LP(des, boo) = LP(de, bo) +1
これは,S,Tの末尾を同じにした場合、,,,

- これらの漸化式を用いて、レーベンシュタイン距離を求める。
全ての遷移において共通しているのは、文字列の末尾を見ること。
なので、1~j~|S|, 1~k~|T| のj,kを用いて、
j>0, k>0 の時

if S[j] == T[k]
    LP[j][k] = min(LP[j-1][k]+1, LP[j][k-1]+1, LP[j-1][k-1])
else :
    LP[j][k] = min(LP[j-1][k]+1, LP[j][k-1]+1, LP[j-1][k-1]+1)

...S[:j], T[:k] までの文字列を取得した際のレーベンシュタイン距離の空間を表した表をLPとする

  b o o k
d 0 1 2 3
e 1
s 2
k 3


##################################################### """
def check() :
    return


def main() :
    S = input()
    T = input()
    LP = [[0 for k in range(len(T)+1)] for j in range(len(S)+1)]
    for j in range(1, len(S)+1) : LP[j][0] = j
    for k in range(1, len(T)+1) : LP[0][k] = k
    
    for j in range(1, len(S)+1) :
        for k in range(1, len(T)+1):
            if S[j-1] == T[k-1] :
                LP[j][k] = min(LP[j-1][k]+1, LP[j][k-1]+1, LP[j-1][k-1])
            else :
                LP[j][k] = min(LP[j-1][k]+1, LP[j][k-1]+1, LP[j-1][k-1]+1)
    print(LP[-1][-1])
    return


if __name__ == "__main__" :
    main()
    #check()
