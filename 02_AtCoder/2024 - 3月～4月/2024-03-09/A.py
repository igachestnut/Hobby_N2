def cheaker() :
    return


def main() :
    s = input()
    
    count = 0
    start = 0
    end = 0
    for i in range(len(s)) :
        if s[i] == "|" :
            if count == 0 :
                start = i
                count+=1
            else :
                end = i+1    
    output = s[0:start] + s[end:]
    print(output) 
    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
