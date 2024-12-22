def cheaker() :
    return


def main() :
    k, s, t = map(int, input().split())
    k_level = ["ABC" for i in range(k-1)] #最小レベルはABCを追加するだけ。
    
    str_i = 0
    level_i = 0
    result = ""
    while str_i <= t :
        if k_level[level_i][0] == "C" :
            result += k_level[level_i][0]
            str_i += 1
            k_level[level_i] = "ABC"
            level_i -= 1
        else :#ABの場合
            result += k_level[level_i][0]
            str_i += 1
            k_level[level_i] = k_level[level_i][1:] #レベル文字列のメモ
            
            if level_i == k-2 :#これ以上深く潜れない場合。
                result += "ABC"
                str_i += 3
            else :                
                level_i += 1
    print(result[s-1:t])
            
        
    return


if __name__ == "__main__" :
    main()
    #cheaker()
