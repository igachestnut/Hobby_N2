def cheaker(s,t) :
    for j in range(len(t)) :
        if s[j] == "?" or t[j] == "?" :
            pass
        elif s[j] != t[j] :
            return "No"
    return "Yes"

def main() :
    S = input()
    T = input()
    lens,lent = len(S),len(T)
    num = lens - lent

    for i in range(lent + 1) :
        print(cheaker(S[:i] + S[num+i:],T))

if __name__ == "__main__" :
    main()
