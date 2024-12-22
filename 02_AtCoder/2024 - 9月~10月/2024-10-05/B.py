def checker() :
    return


def main() :
    S = input()
    T = input()
    myS, myT = [None for i in range(101)], [None for i in range(101)]
    for i, s in enumerate(S) : myS[i] = s 
    for i, t in enumerate(T) : myT[i] = t

    for i in range(101) :
        if myS[i] != myT[i] :
            print(i+1)
            return
    else: print(0)
    return


if __name__ == "__main__" :
    main()
    #checker()
