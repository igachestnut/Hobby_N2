""" #####################################################
発想


##################################################### """
from collections import defaultdict

def check() :
    #a = defaultdict(int)
    #a[2] += 1
    #print(a)
    return


def main() :
    N = int(input())
    A = list(map(int, input().split()))
    numbers = defaultdict(int)
    for a in A : numbers[a] += 1
    result = 0
    for key, value in numbers.items():
        if key <= value : result += value-key
        else : result+=value
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
