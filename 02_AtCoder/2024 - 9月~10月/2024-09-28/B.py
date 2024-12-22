def cheaker() :
    return


def main() :
    S = list(input())
    result = 0

    #Aの位置特定    
    for i in range(26) :
        if ord(S[i]) - ord("A") == 0 : 
            before_i = i

    #B~Zの位置特定
    for i in range(1, 26) :#Aが0でZが25扱いの奴
        for j in range(26) :
            if ord(S[j]) - ord("A") == i :
                #print(f"現在着目している文字がS[j]{S[j]}で、前との距離は。{abs(before_i - j)}でした")
                result += abs(before_i - j)
                before_i = j
                break
            
    print(result)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
