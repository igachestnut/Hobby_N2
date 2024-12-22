""" ############################################################
x = つる, y= kame

cx + dy = a
x + y = b
が成り立つ

#頭の数は決まっているのに、定まらないケース
    c=d (b != 2)のケース？
    
法則性を知るには厳しそう。

一応いうと、入力が全て100以下→全探索が可能なケース
    
    (1) xの数を1から最大数まで全探索するケース
    x = ある数 , y = b-x
    と設定して、
    if (x*c + y*d) == a :
    のケースが2個以上なければ、出力可能 
    
    


########################################################### """



def cheaker() :
    return


def main() :
    Buttonleg, TopHead, turu_leg, kame_leg = map(int, input().split())

    LikelyCase = 0 #あり得る可能性
    X, Y = 1,1     #答え入力用
    for x in range(1, TopHead) :
        y = TopHead-x
        if (x*turu_leg + y*kame_leg) == Buttonleg :
            LikelyCase += 1
            X, Y = x, y
    
    if LikelyCase == 1 :
        print(f"{X} {Y}")
    else :
        print("miss")   
    return


if __name__ == "__main__" :
    main()
    #cheaker()
