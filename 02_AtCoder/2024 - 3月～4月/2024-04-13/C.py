def cheaker() :
    return


def main() :
    S = list(input())
    T = list(input())
    
    #判定するリストの作成
    jugde = [T[0].lower(), T[1].lower()]
    if T[2] == "X" :
        pass
    else :
        jugde.append(T[2].lower())
        
    i = 0
    LEN = len(jugde)
    for s in S :
        if i >= LEN :
            print("Yes")
            return
        if jugde[i] == s :
            i += 1
    if i >= LEN :
        print("Yes")
        return
    else :
        print("No")
        return
        
        
    
    
    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
