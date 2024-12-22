""" 

全数だったらどうするか????
- 1~Nまでのすべての数値をはじめとしたときの、
    - 長さを考える。

- 尺取り法で、最長長さを取得する。
    - 初期条件 l==r==0である。
    - rを動かすケースと、lを動かすケースを整理する。
        - rを動かしたいとき。
        - 初期条件から。
        - r+=1したとき、新規にai が取得できた。この時defaltdict[ai]=0であった。
        - では安直にプラスするのではなく、r+=2したときのai+1 もaiであるか確認する。
            - if 同じとき。正常の値であるため、lを0の状態のまま、rをr+=2の位置までずらすことが可能である。さらにtmp_result+= 2である。
            - else 違うとき、正常な値ではない。
                - 現時点のrと、lを用いて、計算する。resultにmaxとして加算する
                - r=+1にして、これまでのlの全数値を計算する(残っているl)。この場合圧縮しても問題ない。→r=lとしても問題ないさらに、defaltdictを再定義する。
                - lは正常である値なので、 
        - r+=1としたとき、新規にai が取得できたが、この時defaltdict[ai]=2出会った。
            - 現在のlrの最大数を計算する。
            - 安直に加算することはできない。なので、このaiの数値を見つけるまで、lを動かしてあげる。
            - 
    - rを動かす、不正の値→、lの現在位置から、計算する。
    - この繰り返しをi, i+1 が同じじゃなかった場合、r=r+1の位置

"""

def check() :
    return

from collections import defaultdict
def main() :
    """ 尺取り法を使った最長1122列の取得 """
    N = int(input())
    A = list(map(int, input().split()))
    result = 0
    tmp_result = 0
    l, r = -1,-1 #尺取り法 lはみ始め-1の境界、rは文字列に含まない数値
    mydict = defaultdict(int)
    while l < N and r<N :
        r += 1
        if r+1>=N : #次の包含ができなさそう→計算して終了する
            r = N
            result = max(result, tmp_result)
            continue
        elif mydict[A[r]] == 0 : #とりあえず着目したい数値は新規の数値
            print(f"l{l},r{r},A[r]{A[r]}")
            #print(r)
            if A[r] == A[r+1] :  #新規の数値は追加可能であるとき。
                mydict[A[r]] = 2
                tmp_result += 2
                r+=1 #正常の値だったので、rをずらしてあげる
            else :#これ以上数値は存在しないand 不正な数値だった場合→計算する
                result = max(tmp_result, result)
                l = r #最大値を計算したため、これより以下はもう計算する必要なし
                tmp_result = 0
                mydict = defaultdict(int)
        elif mydict[A[r]] == 2 :#数値がすでに追加されている場合。
            print(f"l{l},r{r},A[r]{A[r]}")
            result = max(result, tmp_result) 
            while mydict[A[r]] != 0 :
                print(mydict)
                mydict[A[l+1]] -=2
                tmp_result -= 2
                l+=2
            r-=1
            continue
        else :
            raise ValueError("reigai")

    print(max(result,tmp_result))


    return


if __name__ == "__main__" :
    main()
    #check()
