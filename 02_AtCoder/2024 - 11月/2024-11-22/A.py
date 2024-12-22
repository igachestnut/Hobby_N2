def check() :
    return


def main() :
    N = int(input())
    S = input()
    if N%2 == 0:
        print("No")
        return
    
    strings = [0, 0, 0] #1,/,2 を格納する個数
    for i in range(N) :
        if S[i] == "1" :
            if strings[1] == 0 :
                strings[0] += 1
            else :
                print("No")
                return
        elif S[i] == "/" :
            strings[1] += 1
        else :
            if strings[1] == 1 :
                strings[2] += 1
            else :
                print("No")
                return
    if strings[1] != 1 or strings[0]!=strings[2]:
        print("No")
    else :
        print("Yes")
    return


if __name__ == "__main__" :
    main()
    #check()
