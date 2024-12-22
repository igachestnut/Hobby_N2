def cheaker() :
    return


def main() :
    S = input()
    
    Substrig = set([])
    for i in range(len(S)) :
        for j in range(i+1) :
            Substrig.add(S[j:i+1])
            #print(Substrig)
    print(len(Substrig))
    return


if __name__ == "__main__" :
    main()
    #cheaker()
