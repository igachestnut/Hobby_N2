""" #####################################################
発想

- sを最も早くする
- tを最も遅くする
- s<tになるかどうか判断する。
##################################################### """
def check() :
    return


def main() :
    s = input()
    t = input()
    sn,tn = [],[]
    for i in range(len(s)): sn.append(ord(s[i])-ord("a"))
    for i in range(len(t)): tn.append(ord(t[i])-ord("a"))
    sn.sort()
    tn.sort(reverse=True)
    if len(s) == len(t) :
        pass
    elif len(s) > len(t) :
        for i in range(len(s)-len(t)) :
            tn.append(-1)
    else :
        for i in range(len(t)-len(s)) :
            sn.append(-1)
    
    for i in range(len(tn)) :
        if sn[i] == tn[i] : 
            continue
        elif sn[i] > tn[i] :
            print("No")
            return
        else :
            print("Yes")
            return
    print("No")
    return

def main2() :
    """ 解答に衝撃的なやり方があった。もう文字列比べられるらしい """
    s = input()
    s_asc = ''.join(sorted(s))

    t = input()
    t_desc = ''.join(sorted(t, reverse=True))

    if s_asc < t_desc:
        print('Yes')
    else:
        print('No')
    return

if __name__ == "__main__" :
    main()
    #check()
