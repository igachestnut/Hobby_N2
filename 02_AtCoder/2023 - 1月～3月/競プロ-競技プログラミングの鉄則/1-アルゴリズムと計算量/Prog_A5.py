#脳死全数調査
def all_cheaker(n,k) :
    """処理時間O(N**3)"""
    count = 0
    for x in range(1,n+1) :
        for y in range(1,n+1) :
            for z in range(1,n+1) :
                if x+y+z == k :
                    count += 1
    return count


#条件＋
def cheaker2(n,k) :
    """
    二つが決まるともう一つが決まるという
    法則を活用する。
    　処理時間O(N**2)
    """
    count = 0
    for x in range(1,n+1) :
        for y in range(1,n+1) :
            z = k - x - y
            if 0 < z <= n :
                count += 1
    return count
                
#グラフアルゴリズム？（DFS）
def DFS() :
    """処理時間O(N)解法はあるのだろうか"""
    return

def main() :
    N,K = map(int,input().split())
    print(cheaker2(N,K))

if __name__ == "__main__" :
    main()
    
