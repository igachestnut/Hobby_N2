def cheaker() :
    return


import bisect
def main() :
    M = int(input())
    
    three_pows = [1] + [3**i for i in range(1,11)]
    result = []
    while M > 0 :
        r = bisect.bisect(three_pows, M)-1
        result.append(r)
        M -= three_pows[r]
    print(len(result))
    print(*result)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
