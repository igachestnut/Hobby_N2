def cheaker() :
    return


def main() :
    S = list(str(input()))
    Comment = {}
    for s in S :
        if not s in Comment :
            Comment[s] = 1
        else :
            Comment[s] += 1
            
    #判定のアルゴリズム
    for i in range(1, 101) :
        #dict内に該当する変数が何個あるのかをカウントする
        count_n = 0
        for key, value in Comment.items() :
            if value == i :
                count_n += 1
                #print(key)
        
        #そのカウント合計をチェックする
        if count_n == 0 or count_n == 2 :
            pass
        else :
            print("No")
            return
        
    print("Yes")
    return

        
         
    return


if __name__ == "__main__" :
    main()
    #cheaker()
