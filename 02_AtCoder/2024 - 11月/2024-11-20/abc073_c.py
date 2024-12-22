""" #####################################################
発想


##################################################### """
def check() :
    return

from collections import defaultdict
def main() :
    N = int(input())
    numbers = defaultdict(int)
    for i in range(N) :
        a = int(input())
        if numbers[a] == 0:
            numbers[a] = 1
        else :
            numbers[a] = 0
    result = 0
    for value in numbers.values() :
        if value == 1: result += 1
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
