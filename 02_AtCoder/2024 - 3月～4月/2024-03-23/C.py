def cheaker() :
    return


def main() :
    N,K = map(int, input().split())
    a = list(set(map(int, input().split())))
    a.sort()

    ans = K**2 // 2
    for n in range(len(a)) :
        ans -= a[n]
    print(ans)
    return

def main2() :
    N,K = map(int, input().split())
    a = list(set(map(int, input().split())))
    a.sort()
    
    #aが無かった時の総和を求める
    S = (0+K)//2 * K

    #この値から数値を引く
    for i in range(len(a)) :
        S -= a[i]
        
    print(S)
    return
    
if __name__ == "__main__" :
    main2()
    #cheaker()
