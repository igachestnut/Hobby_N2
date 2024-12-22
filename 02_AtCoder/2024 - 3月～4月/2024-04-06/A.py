def cheaker() :
    return


def main() :
    N = int(input())
    
    result = ""
    for i in range(1, N+1) :
        if i % 3 == 0 :
            result += "x"
        else: 
            result += "o"    
            
    print(result)
        
    return


if __name__ == "__main__" :
    main()
    #cheaker()
