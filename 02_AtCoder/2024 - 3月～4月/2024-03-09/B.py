def cheaker() :
    return


def main() :
    List = []
    while True :
        try :
            Str = int(input()) 
        except EOFError :
            break
        List.append(Str)
    
    for i in range(len(List)) :
        print(List[-1*(i+1)])
    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
