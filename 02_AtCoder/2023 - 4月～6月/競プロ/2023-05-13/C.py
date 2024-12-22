def cheaker() :
    A = input()
    B = input()
        
    countA = 0
    countB = 0
    for i in range(len(a)) :
        if "@" == a[i] :
            counta +=1
        if "@" == b[i] :
            countb += 1

    
    sameA = set(A + B) - set(A)
    if "@" in sameA :
        sameA -= "@"

    sameB = set(A + B) - set(B)
    if "@" in sameA :
        sameA -= "@"
        
    #共通の内容ーb配列⇒A特有の文字
    if counta < len(sameA) :
        return "No"
    if countA < len(sameB) :
        return "No"
    else :
        return "Yes"


def main() :
    A = input()
    B = input()
        
    countA = 0
    countB = 0
    for i in range(len(A)) :
        if "@" == A[i] :
            countA +=1
        if "@" == B[i] :
            countB += 1

    #Aの共通部分外。same = set(A+B)
    sameA = set(A + B) - set(A)
    if "@" in sameA :
        sameA -= "@"

    sameB = set(A + B) - set(B)
    if "@" in sameB :
        sameA -= "@"
        
    #共通の内容ーb配列⇒A特有の文字
    if countA < len(sameA) :
        print("No")
        return 
    if countB < len(sameB) :
        print("No")
        return 
    else :
        print("Yes")
        return 
    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
