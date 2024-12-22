def cheaker() :
    return


def main() :
    N,M = map(int,input().split())
    S = []
    for i in range(M) :
        c = int(input())
        S.append(list(map(int,input().split())))

    a = len(int(bin(M[2:])))
    bit = []
    for i in range(M) :
        b = int(bin(i[2:]))
        bit.append([[0 for i in range(len(a-len(b)))] + [b]])
        
    for i in range(len(bit)) :
        for j in range(N) :
            if 
        
    return


if __name__ == "__main__" :
    main()
    #cheaker()

def memo() :
    """
    bit全探索を効率的に出力する方法が分からない
    pythonで形よく適当な感じで早く出力したいけど、力技しか思いつかない
    """
