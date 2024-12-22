""" #####################################################
発想


- ABという文字列を作る
先頭がB or 末尾がA であるか。
- AB というのが何個含まれているか, 

- 別々のオブジェクトにおいて、一つ一つのつながりがある
- 末尾A only, 先頭B only, 末尾A先頭B
- 

AB_count を数え上げる。
BxxA, Bxxx, xxxA を数え上げる。



##################################################### """
def check() :
    return


def main() :
    N = int(input())
    AB_count = 0
    BxxA, Bxxx, xxxA = 0,0,0
    for i in range(N) :
        Si = input()
        for j in range(len(Si)-1) :
            if Si[j:j+2] == "AB" :
                AB_count += 1
        if Si[0] == "B" and Si[-1] == "A" :
            BxxA += 1
        elif Si[0] == "B" :
            Bxxx += 1
        elif Si[-1] == "A" :
            xxxA += 1
    
    # うまい感じにつなげてABを作成する。(1)BAの全つなげ
    if BxxA > 0 :
        AB_count += BxxA-1
        if Bxxx > 0 :
            Bxxx -= 1
            AB_count += 1
        if xxxA > 0 :
            xxxA -= 1
            AB_count += 1
        AB_count += min(Bxxx, xxxA)
    else :
        AB_count += min(Bxxx, xxxA)
    print(AB_count)
    return


if __name__ == "__main__" :
    main()
    #check()
