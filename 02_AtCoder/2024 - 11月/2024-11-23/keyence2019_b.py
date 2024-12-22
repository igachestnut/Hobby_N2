""" #####################################################
発想

keyenceを作ることができるのか?
- kから始まるすべてのkeyenceを取得する。
    strings = []
- 各配列に対して、1,2,3,4,5,6,7を減算し、x1orx2(2つのindex)で構成されているならTrue、それ以外ならFalse
- 要素の量に関しては、setを使って判断する。1の場合は引かなくても答えが正解であるということ

...もしかしたら、
aakeyenceaa の場合
1回切り取っても、出力はkeyenceにはならない。これがコーナーケースとなっていそう。

kkeeyence の場合、keを切り抜くと、keyenceになるが、答えはFalseになってしまう
[[0, 2, 4, 5, 6, 7, 8]] のようだ。この2を3として抜き出せば答えは出そうである。


- もう一度考え直す。
- 正解パターンは
    1. xxxxkeyence という左に不要文字 → S[-7:]==keyence
    2. keyencexxxx という右に不要文字 → S[:7] ==keyence
    3. keyxxxence 間に不要文字。
        - 左からkey, 右からenceである。数えられるだけ調査して、OKなら終了、

#################################################### """
def check() :
    return


def main() :
    S = input()
    strings = []
    find_str = "keyence"
    for i in range(len(S)) :
        if S[i] == "k" :
            # 該当文字を全て見つけその時のindexを格納する。
            tmp_str = []
            if i>0 : tmp_str.append(-10)
            j=0
            for fs in find_str:
                while i+j<len(S) and S[i+j] != fs: j+=1
                if i+j>=len(S): break
                else :
                    tmp_str.append(i+j)
            if len(tmp_str) != 7: 
                break
            else :
                if i+j < len(S)-1: tmp_str.append(120) #追加した文字が最後の要素ではない場合。
                strings.append(tmp_str)
    
    print(strings)
    for k,string_index in enumerate(strings) :
        set_s = set()
        for j,s in enumerate(string_index): set_s.add(s-j)
        if len(set_s) < 3 :
            print("YES")
            return
    print("NO")
    return

def main2():
    """ 正解から調査する方向性 """
    S = input()
    ac_str = "keyence"
    if S[-7:] == ac_str or S[:7] == ac_str:
        print("YES")
        return
    else :
        result = [False] *7
        for i in range(7) :
            if ac_str[i] == S[i]:
                result[i] = True
            else : break
        for i in range(1, 8) :
            if ac_str[-i] == S[-i] :
                result[-i] = True
            else :
                break
        if all(result) :
            print("YES")
            return
    print("NO")
    return

if __name__ == "__main__" :
    main2()
    #check()
