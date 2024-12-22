def cheaker() :
    return


def main() :    
    N,K = map(int,input().split())
    a = set(map(int,input().split()))
    
    for i in range(K) :
        if i not in a :
            print(i)
            return
    else :
        print(i+1)
    return

if __name__ == "__main__" :
    main()
    #cheaker()

def memo() :
    """
    MEXとは
    配列に含まれない最小の非負整数
    
    
    """
