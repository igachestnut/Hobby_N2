def cheaker() :
    return


def main() :
    N, A = map(int, input().split())
    T = list( map(int, input().split()))
    
    result = 0
    for i in range(N) :
        if result < T[i] : #お客さんがいない場合
            result = T[i] + A
        else : 
            result += A
        print(result)    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
