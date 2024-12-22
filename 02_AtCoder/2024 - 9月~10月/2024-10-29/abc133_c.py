""" #####################################################
発想


選ぶ通り= 2*10**9 C 2 である。
→全数は間に合わない。

2019 がmodである。
余りの演算には何か傾向があったはず。

とりあえずi,jのどちらかが2019の場合、必ず答えが0になる。
2020*2 と1*2021の答えが一緒になるはず。

→なので、与えられたL,Rから、2019以内の長さのmod配列を作成する。

最初の問題提起を修正すると、2019C2を解く問題になる。
...これなら全数はなんとか行けそう。

##################################################### """
def check() :
    mod = 2019
    print(2021*1 %mod)
    print(2*2020 %mod)
    return


def main() :
    L, R = map(int, input().split())
    
    if R-L >= 2019 : 
        print(0)
        return
    
    mod_2019 = []
    for i in range(L, min(R+1, L+2019)) :
        mod_2019.append(i % 2019)
    
    # 2019 C 2 の全数調査
    result = float("inf")
    for i in range(len(mod_2019)) :
        for j in range(i+1, len(mod_2019)) :
            result = min(result, (mod_2019[i]*mod_2019[j])%2019)
            #print(result)
    
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
