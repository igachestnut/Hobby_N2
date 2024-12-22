""" #####################################################
発想


##################################################### """
def cheaker() :
    return


def main() :
    S = input()
    strings = list(S)
    
    low = 0
    up = 0
    
    for s in strings :
        if s.isupper() :
            up += 1
        else :
            low += 1
    
    if low > up :
        print(S.lower())
    else :
        print(S.upper())    
    
    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
