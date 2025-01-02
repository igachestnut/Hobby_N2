""" #####################################################
発想

- SをTに変更できるか判定。

条件達成のためのMEMO
1. 出現する種類数が一緒であること。
2. 構成される種類ごとの数値が一致していること。

...よって
1. 種類数setと、文字数数え上げ
2. 種類数set比較
3. 出てきた数値
##################################################### """
def check() :
    return


def main() :
    S = input()
    T = input()

    S_set, T_set = set(),set()
    S_cnt, T_cnt = [0]*26, [0]*26
    for s,t in zip(S,T) :
        S_set.add(s)
        T_set.add(t)
        S_cnt[ord(s)-ord("a")] += 1
        T_cnt[ord(t)-ord("a")] += 1
    
    if len(S_set) != len(T_set) :
        print("No")
    else :
        S_cnt.sort()
        T_cnt.sort()
        if S_cnt != T_cnt :
            print("No")
        else :
            print("Yes")
    return


if __name__ == "__main__" :
    main()
    #check()
