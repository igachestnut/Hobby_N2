def cheaker() :
    return


def main() :
    N = int(input())
    
    Map = [list(map(int,input().split()), i+1) for i in range(N)]
    Map = sorted(Map, key=lambda:x[0] for x in Map)
    print(Map)
    """
    result1 = [[10**10, 10**10]]
    #方法　左から1回右から1回
    for n in range(N) :
        a, c = map(int, input().split())
        if result[-1][0] < a or result[-1][1] > c :
            result1.append([a, c])
    """
    return


if __name__ == "__main__" :
    main()
    #cheaker()
