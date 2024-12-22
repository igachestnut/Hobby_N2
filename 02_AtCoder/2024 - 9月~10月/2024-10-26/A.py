def check() :
    return


def main() :
    S = input()
    abc = [0, 0, 0]
    for i in range(3) :
        if S[i] == "A" :
            abc[0] += 1
        elif S[i] == "B" :
            abc[1] += 1 
        elif S[i] == "C" :
            abc[2] += 1
        else :
            print("No")
            return
    if abc == [1, 1, 1] :
        print("Yes")
    else :
        print("No")
    return


if __name__ == "__main__" :
    main()
    #check()
