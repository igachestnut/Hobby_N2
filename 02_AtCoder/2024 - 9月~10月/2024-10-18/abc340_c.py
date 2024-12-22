""" #####################################################
発想


##################################################### """
def check() :
    return


def main() :
    """ シンプルな実装 TLE """
    numbers = [int(input())]

    result = 0
    while numbers != [] :
        x = numbers.pop()
        if x <= 1 : continue

        x_harf = x//2
        if x % 2 == 0 : 
            numbers.append(x_harf)
            numbers.append(x_harf)
        else : 
            numbers.append(x_harf+1)
            numbers.append(x_harf)        
        result += x

    print(result)
    return

def main2() :
    pass
if __name__ == "__main__" :
    main()
    #check()
