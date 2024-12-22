def check() :
    return


def main() :
    N = int(input())
    a = list(map(int, input().split()))
    mod_e, mod_two, mod_four = 0, 0, 0 
    for i in range(N) :
        if a[i] %2 != 0 :
            mod_e += 1
            continue
        else :
            if a[i] %4 != 0:
                mod_two += 1
            else :
                mod_four += 1

    if mod_two == 0 :
        if mod_four >= mod_e-1 : 
            print("Yes")
        else :
            print("No")
    else :
        if mod_four >= mod_e : 
            print("Yes")
        else :
            print("No")
    return


if __name__ == "__main__" :
    main()
    #check()
