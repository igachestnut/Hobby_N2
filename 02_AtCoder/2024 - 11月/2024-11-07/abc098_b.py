""" #####################################################
発想

0 ~ N-1 のSにおいて
1~N-2まで実行(切る処理)

同じ文字が出る数の最大化

a が10この文字列の場合
a aaaaaaaaa


2つX,Y 作って、ordで配列管理して、
min(X[i],Y[i])でいいんじゃね？




##################################################### """
def check() :
    return


def main() :
    N = int(input())
    S = input()

    X, Y = [0]*26, [0]*26
    for i in range(N) :
        Y[ord(S[i])-ord("a")] += 1
    
    result = 0
    for i in range(N-1) :
        tmp_result = 0 #1回の検証における結果
        ai = ord(S[i])-ord("a") #alphabet index の意
        X[ai] += 1
        Y[ai] -= 1 
        for j in range(26) :
            if min(X[j], Y[j]) > 0 :
                tmp_result += 1
        result = max(result, tmp_result)
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
