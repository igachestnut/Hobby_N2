def cheaker() :
    return


def main() :
    N = int(input())
    T = []
    max_Si = 0
    for i in range(N) :
        s = list(input())
        max_Si = max(max_Si, len(s))
        #箱枠作成
        if len(T) < max_Si :
            for m in range(max_Si-len(T)) :
                T.append([])
        #print(T)
        
        #新規文字列を左上から代入していく。
        for j in range(max_Si) :
            if j < len(s) :
                T[j].append(s[j])
            else :
                T[j].append("*")
        
    for j in range(len(T)) :
        result = "".join(reversed(T[j]))
        print(result)
        
        
    return


if __name__ == "__main__" :
    main()
    #cheaker()
