def cheaker() :
    return


def main() :
    S = list(input())
    
    S.sort()
    for i in range()
    
    return


def main2() :
    
    S = list(input())
    cat_S = list(set(S))
    N = list()
    
    for i in range(len(cat_S)) :
        n = 0
        for j in range(len(S)):
            if cat_S[i] == S[j]:
                n += 1
        N.append(n)
    N.sort()
    if (len(N)%2) != 0:
        print("No")
        return
    if (len(N) != len((set(N)))*2):
        print("No")
        return
    for i in range(0,len(N),2):
        if N[i] == N[i+1]:
            pass
        else:
            print("No")
            return
    print("Yes")
    return

        
             
    
    


if __name__ == "__main__" :
    main2()
    #cheaker()
