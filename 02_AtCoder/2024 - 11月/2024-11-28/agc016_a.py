""" #####################################################
発想

- 単一の文字のみにしたい！
- 文字を引き継げるのは、i+1の文字のみ。
- ケツは削除されていく。

愚直な全数調査を考える。
- 結局は同じアルファベットにしたいということなので、
a~zまでそれぞれ最小回数を調査するとよさそう。
len(s) <100だから余裕そう。
- 全てのaに対して、aを上塗りしていく。という処理
1回の調査に、100(len(s))だけ調査して、それを100回繰り返せば、
一応答えは出そう
26*len(S)*len(S) < 10**6 で高速

-flow
1. aに着目するとする。
2. for j in range(len(tmp_s)-1) :
3. もしaをi+1で発見したとき、現在の値をaにする。aに書き換えるとややこしいので、1,0にしてもいいかも?
4. 
 
##################################################### """
def check() :
    return


def main() :
    S = input()
    result = float("inf")
    for ai in range(26) :
        # 該当のアルファベットに着目した01配列を作る。
        tmp_S = []
        count = 0
        for s in S:
            if ord(s)-ord("a") == ai: 
                tmp_S.append(1)
                count += 1
            else: 
                tmp_S.append(0)

        #該当のアルファベットが存在しないなら
        if count == 0 :
            continue

        # 全てが1で構成されるまで実施
        while count != len(tmp_S) :
            new_tmp_S = []
            for j in range(len(tmp_S)-1):
                if tmp_S[j] == 1 : 
                    new_tmp_S.append(1)
                elif tmp_S[j+1] == 1: 
                    new_tmp_S.append(1)
                    count+=1
                else :
                    new_tmp_S.append(0)
            if tmp_S[-1] == 1: count-=1
            tmp_S = new_tmp_S
        result = min(len(S)-len(tmp_S), result)
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
