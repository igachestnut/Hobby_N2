def cheaker() :
    a = -1 //5
    print(a)
    return


def main() :
    w, b = map(int, input().split())
    
    #文字列の長さの取得
    LEN = w+b
    
    #必ず発生するRoop数を取得
    roop = LEN // 12
    
    #roopの端の算出
    w = w - (7*roop)
    b = b - (5*roop)
    
    LEN_side = w+b
    if LEN_side == 0 :#0の時プラスになってしまう為
        LEN_side = 1
    #必ず出てくる形の数の算出
    five_brock = (LEN_side-1) // 5
    
    w = w - (3*five_brock)
    b = b - (2*five_brock)
    
    #これにより0～4までのlenをもった文字列が完成する
    if judge(w,b) :
        print("Yes")
    else :
        print("No")
    
    
    
def judge(w,b) :
    if w < 0 or b < 0 :
        return False
    
    #小さい数における条件判定   
    elif w+b == 0 :
        return True
    elif w+b == 1 :
        return True
    elif w+b == 2 :
        if b == 2 :
            return False
        else :
            return True
    elif w+b == 3 :
        if w == 3 or b == 3 :
            return False
        else :
            return True
    elif w*b == 4 :
        if w==4 or b == 4 or b == 3 :
            return False
        else :
            return True
    else :
        if w==5 or b==5 or w==4 or b==4:
            return False
        else :
            return True
    
    
    
    
    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
