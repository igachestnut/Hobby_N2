def cheaker() :
    return


def main() :
    S = list(input())
    T = list(input())
    X = []

    if S == T :
        print(0)
        return
    
    for i in range(len(S)) :
        if ord(S[i]) > ord(T[i]) :
            S[i] = T[i]
            X.append("".join(S))
            
    for i in range(len(S)-1, -1, -1) :
        #print(i)
        if ord(S[i]) < ord(T[i]) :
            S[i] = T[i]
            X.append("".join(S))
            
    print(len(X))
    for x in X :
        print(x)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
