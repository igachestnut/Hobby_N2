def check() :
    return


def main() :
    N = input()
    result = [False] *3
    for i in range(3) :
        count = 0
        for j in range(6) :
            if N[j] == str(i+1) :
                count +=1
        result[i] = count
    
    if result == [1,2,3] :
        print("Yes")
    else :
        print("No")
    return


if __name__ == "__main__" :
    main()
    #check()
