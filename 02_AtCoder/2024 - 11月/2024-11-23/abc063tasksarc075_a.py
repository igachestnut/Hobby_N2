""" #####################################################
発想

画面に表示される数字の最大数を出す。
答えがr%10==0 の時 r//10されてしまう。

- 答えの全数調査をする。
- ナップサック問題と同義である。
- 配点の種類は2**N だけ存在する。
- 制約が100なので、100*N <10**4 までのdpを定義して解いてもいいし、queueに格納して解いてもいい。

..
BFSっぽく作ったが、
計算回数に2**Nだけ必要としそうな書き方である。
制約がs<100であるため、1回の処理で確認すべき配列の最大数が10**4以内であるため、間に合うが、
これ以上の制約には対応できない


... 成績が10の倍数だった時、答えは0である
##################################################### """
def check() :
    return


def main() :
    N = int(input())
    points = set([0])
    for i in range(N) :
        new_queue = points
        s = int(input())
        for que in list(points) :
            new_queue.add(que+s)
        points = new_queue
    #print(points)
    result = 0
    for p in points :
        if p%10==0 : continue
        result = max(result, p)
    
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
