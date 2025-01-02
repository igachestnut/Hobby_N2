""" #####################################################
発想


##################################################### """
def check() :
    a = "aaabaaa"
    a = sorted(a)
    print(a)
    return


from collections import defaultdict
def main() :
    N = int(input())
    
    strings = defaultdict(int)
    for i in range(N) :
        s = "".join(sorted(input()))
        strings[s] += 1
    
    result = 0
    for key,value in strings.items() :
        if value > 1 :
            result += value*(value-1)//2
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
