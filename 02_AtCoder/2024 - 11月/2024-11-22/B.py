def check() :
    return


def main() :
    S = input()
    alphabet = [0 for i in range(26)]
    if len(S)%2 ==1 :
        print("No")
        return
    
    for i in range(0, len(S), 2) :
        if S[i] == S[i+1] :
            alphabet[ord(S[i])-ord("a")] += 1
        else :
            print("No")
            return
        
    for a in range(26) :
        if alphabet[a] > 1 :
            print("No")
            return
    else :
        print("Yes")
    return


if __name__ == "__main__" :
    main()
    #check()
