""" #####################################################
発想

- 隣り合う2つのタイルがすべて異なるようにしたい。

- 結果したいもの
010101
101010
だけ。
上記2つを調査して、小さいほうが答え

##################################################### """
def check() :
    return


def main() :
    S = input()
    if len(S)==1: 
        print(0)
        return
    result = float("inf")
    tmp_r_101 = 0 # 101010..にならなかった数
    for i in range(0,len(S)-1,2) :
        tmp_r_101 += 1 if S[i]=="1" else 0
        tmp_r_101 += 1 if S[i+1]=="0" else 0
    if len(S)%2==1: tmp_r_101 += 1 if S[-1]=="1" else 0
    result = min(result, tmp_r_101, len(S)-tmp_r_101)
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
