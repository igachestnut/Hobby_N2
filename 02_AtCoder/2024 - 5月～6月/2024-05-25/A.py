def cheaker() :
    return


def main() :
    A, B = map(int, input().split())
    
    result = [True, True, True]
    result[A-1] = False
    result[B-1] = False
    
    if sum(result) > 1 :
        print(-1)
    else :
        for r in range(len(result)) :
            if result[r] :
                print(r+1)
                break       
    return


if __name__ == "__main__" :
    main()
    #cheaker()
