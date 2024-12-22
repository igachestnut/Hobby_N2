def cheaker() :
    return


def main() :
    N = int(input())
    
    #使う情報→その色codeにおける最小値
    worst_tasting = {}
    
    for n in range(N) :
        tast, color = map(int, input().split())
        if color not in worst_tasting :
            worst_tasting[color] = tast
        elif worst_tasting[color] > tast :
            worst_tasting[color] = tast
        else :
            pass
        
    #色ごとの最小値をまとめたdistの出力
    #print(worst_tasting)
    #最大値
    print(max(worst_tasting.values()))
    
    
    
    
    return

if __name__ == "__main__" :
    main()
    #cheaker()
