""" MEMO

https://algo-logic.info/warshall-floyd/

"""
def checker() :
    return


def main() :
    """ ワーシャルフロイド法の実装 """
    N, M = map(int,input().split())
    dist = [[float("inf") for j in range(N)] for i in range(N)]
    for i in range(N): dist[i][i] = 0
    for m in range(M) :
        a, b, c = map(int, input().split())
        dist[a-1][b-1] = c

    # kを経由しての値の作成。kを0から行う。
    result = 0
    for k in range(N) :
        for i in range(N) :
            for j in range(N) :
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
                if dist[i][j] != float("inf") : result += dist[i][j]

    
    print(result)
    return


if __name__ == "__main__" :
    main()
    #checker()
