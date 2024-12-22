""" #####################################################
発想


##################################################### """
from collections import defaultdict

def cheaker() :
    return


def main() :
    N = int(input())
    A = list(map(int, input().split()))

    d = defaultdict(list)
    for i, ai in enumerate(A) : d[ai].append(i)
    
    ans = 0
    for a in d.keys() :
        ans += N*(N+1)//2
        d[a].append(N)
        l = -1
        for r in d[a] :
            k = r - l -1 #各iを構成するindexの間を調査する。
            ans -= k*(k+1)//2
            l = r
    print(ans)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
