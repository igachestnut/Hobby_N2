def cheaker() :
    return


def main() :
    N = int(input())
    L_all, R_all = 0, 0
    L, R = [], []
    for i in range(N) :
        l, r = map(int, input().split())
        L_all += l
        R_all += r
        L.append(l)
        R.append(r)
        
    if L_all <= 0 <= R_all :
        print("Yes")
    else :
        print("No")
        return
    
    add_number = abs(L_all)
    result = []
    for n in range(N) :
        if add_number > 0 :
            local_add = min(R[n] - L[n], add_number)
            result.append(L[n]+local_add)
            add_number -= local_add
        else :
            result.append(L[n])
            
    print(*result)    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
