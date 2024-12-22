def cheaker() :
    return


def main() :
    S, T = input().split()
    
    for i in range(2, len(S)) :#c 分割する文字数 2文字から、|S|-1文字目まで (2文字目以降T<Sより)
        tmp_string = ""
        for j in range(i-1, len(S), i) :#
            tmp_string += S[j]
        print(tmp_string)
        if tmp_string == T :
            print("Yes")
            return
    else :
        print("No")        
    return


if __name__ == "__main__" :
    main()
    #cheaker()
