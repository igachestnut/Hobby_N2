""" #####################################################
発想


- 鍵を特定する問題
- 鍵のヒントとしてS,T が与えられる。
- Sは虫食いのような感じ
- Tは必ず入っている文字列。
- 想定できるキーのうち、辞書順で最小を出力しろ。


- 想定される辞書順で最も早い→? は必ずa と変換される
- 想定される辞書順で最も早い→複数の???がある中だったら、最も後ろのを参照する。

- 全数調査
    - |S|-|T| ~ 0 のiについて,|T|だけ抜き出した文字列siを考える。(配列の後ろから)
    - Tとsi が???を除いて完全一致の時、答えとなる文字列のi~i+|T|の部分をTに書き換える。
    - 出力

- 計算量
    - 50 かい抜き出して考える len(S)
    - 各調査に最大50回調査する len(T)
    - 結果がわかった場合、lenTかい変換処理
    ...よって O(S*T+T)

##################################################### """
def check() :
    return


def main() :
    Sd = list(input())
    T = list(input())
    S = [s if s != "?" else "a" for s in Sd]

    for i in range(len(Sd)-len(T), -1, -1) :
        tmp_s = Sd[i:i+len(T)+1]
        #print(tmp_s)
        r = True
        for j in range(len(T)) :
            if tmp_s[j] == "?" :
                pass
            elif tmp_s[j] == T[j] :
                pass
            else :
                r = False
                break

        if r == True :
            for j, t in enumerate(T) :
                S[i+j] = t
            print("".join(S))
            return
    else :
        print("UNRESTORABLE")
    return


if __name__ == "__main__" :
    main()
    #check()
