def cheaker() :
    return


def main() :
    List = create_()

    Q = int(input())
    X = list(map(int, input().split()))
    
    for x in range(len(X)) :
        Bool = binary_search(List, X[x])
        if Bool :
            print("Yes")
        else :
            print("No")
 
        

def create_() :
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    
    #全ての生成できる配列を作成する。
    d = set([])
    for i in range(n) :
        for j in range(m) :
            d.add(a[i]+b[j])
    d = list(d)

    l = int(input())
    c = list(map(int, input().split()))        
    e = set([])
    for i in range(len(d)) :
        for j in range(l) :
            e.add(d[i]+c[j])
    e = list(e)
    e.sort()    
    return e

def binary_search(List, t) :
    """ 二分探索を使った判別
    
    Parameters
    -------------
    List :
        判定に用いる全ての数字が入ったリスト
    t:
        判別したい数字

    Return
    --------
    bool :
        tが存在するか否かを出力する
    """
    #print(List)
    top, last = 0, len(List)-1
    while top != last :
        
        #print("top", top)
        #print("last", last)
        mid = (top + last + 1) // 2 #半分に割って、上の方を調査
        #print(mid)
        if List[mid] > t :
            last = mid -1 #tの方が小さいすなわち、それ以上に存在しない。
        else :
            top = mid #tの方が大きいすなわち、それ未満に存在しない。
        
    if List[last] == t :
        return True
    else :
        return False


if __name__ == "__main__" :
    main()
    #cheaker()
