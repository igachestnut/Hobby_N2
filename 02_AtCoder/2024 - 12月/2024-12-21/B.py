def check() :
    return


def main() :
    """ 
     
    Note
    - X,Y = サンタさんの初期位置
    - Tというqueryが与えられるので、移動可能なら実施する
    """
    H,W,X,Y = map(int, input().split())
    S = []
    S.append(["#"]*(W+2))
    for h in range(H) :
        S.append(["#"] + list(input()) + ["#"])
    S.append(["#"]*(W+2))
    T = list(input())
    #for s in S: print(s)

    result_set = set()
    for t in T :
        if t == "U" :
            if S[X-1][Y] == "#" :
                pass
            else :
                X -=1
                if S[X][Y] == "@" :
                    result_set.add(X*W + Y)
        elif t == "D" :
            if S[X+1][Y] == "#" :
                pass
            else :
                X +=1
                if S[X][Y] == "@" :
                    result_set.add(X*W + Y)
        elif t == "L" :
            if S[X][Y-1] == "#" :
                pass
            else :
                Y -=1
                if S[X][Y] == "@" :
                    result_set.add(X*W + Y)
        else :
            if S[X][Y+1] == "#" :
                pass
            else :
                Y +=1
                if S[X][Y] == "@" :
                    result_set.add(X*W + Y)
    result = [X,Y,len(result_set)]
    print(*result)
    return


if __name__ == "__main__" :
    main()
    #check()
