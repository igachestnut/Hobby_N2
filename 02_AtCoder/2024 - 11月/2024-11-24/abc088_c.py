""" #####################################################
発想


- b2-b1, b3-b1 を作り出す。
c12:c33の配列を、c11~c31 (各行)でマイナスすると、残る数値は
 b2-b1(2列目), b3-b1(3列目)となる。
 あとは列ですべてのindexが同じかどうか調べる



   b1,   b2,   b3
a1|a1b1, a1b2, a1b3|3a1 +b1+b2+b3
a2|a2b1, a2b2, a2b3|3a2 +b1+b2+b3
a3|a3b1, a3b2, a3b3|3a3 +b1+b2+b3
   
a1行の総和 3a1 +b1+b2+b3




##################################################### """
def check() :
    return


def main() :
    C = []
    for i in range(3) :
        C.append(list(map(int, input().split())))
    
    result = "Yes"
    for i in range(3): #減算に使用する位置
        for j in range(1,3) :#減算される位置 1,2 or 2,3 or 3,1
            j = (i+j)%3
            # 列の調査 bj-bi が同じ値か見る。正確には, bj-bi=(a1+bj)-(a1+bi)
            if C[0][j]-C[0][i] == C[1][j]-C[1][i] == C[2][j]-C[2][i]: pass
            else: result = "No"

            # 行の調査 bj-b1
            if C[j][0]-C[i][0] == C[j][1]-C[i][1] == C[j][2]-C[i][2]: pass
            else: result = "No"
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
