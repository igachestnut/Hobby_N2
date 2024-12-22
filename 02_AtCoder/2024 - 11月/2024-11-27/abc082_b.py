""" #####################################################
発想

- tの文字列において、一つでもsi<ti となる文字列が存在すればYesになりそう。
    - s = abcdefgh
    - t = abcdefa
    ...アルファベットの番号を1~j~26とすると、
    ...1 つでもというより、sa[j] < ta[j]

アルファベットの種類をindexとしたときの、数を記すリストを
sa, taとし、
0~j~25 において、
sa[j]<ta[j]を見つける。

s = cd
t = abc
s の中で一番早い数値がtの最も遅い数値の数よりも多いか否かを調べるとよさそう


##################################################### """
def check() :
    return


def main() :
    """ 
    """
    S = input()
    T = input()
    sa,ta = [0]*26, [0]*26
    for si in S: sa[ord(si)-ord("a")] += 1
    for ti in T: ta[ord(ti)-ord("a")] += 1
    for j in range(25, -1, -1) :
        if sa[j] < ta[j] :
            print("Yes")
            return
    else :
        print("No")
    return

def main2() :
    """ Sのうち最も早い辞書番号の種類とその数< Tのうち最も遅い辞書番号の種類とその数 """
    S = input()
    T = input()
    sa,ta = [0]*26, [0]*26
    for si in S: sa[ord(si)-ord("a")] += 1
    for ti in T: ta[ord(ti)-ord("a")] += 1
    ################
    return



if __name__ == "__main__" :
    main2()
    #check()
