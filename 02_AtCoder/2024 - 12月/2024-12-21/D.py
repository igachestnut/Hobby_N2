""" ################

- (i,j) (X,Y)に家が建っている※注意xが縦,yが横
- M回のquery
- X,Y に家がある。
- 移動経路上に家があるか、全列挙する

- 直線に移動する。

...
効率的に1次元配列から、a,bの取り出す方法がありそう。


################# """

def check() :
    a = dict()
    a[1] = [-10**9, 1,3,6, 10**9]
    #a[1].append(3)
    s = bisect.bisect_left(a[1], 0)
    e = bisect.bisect_left(a[1], 2)
    print(s,e)
    return

import bisect
def main() :
    """ 
    
    flow
    1. 縦方向、横方向に着目したmapを作る
    2. queryの実行
        - 縦なら、縦のdict 参照。
        - 存在しない→pass , 
        - 存在する、bisect で値を取得。 家があるならその座標を取得、横の家マップに反映(該当のindex はbisect)

    - 計算量
        - 家の定義 2N
        - 調査 M
        - 家の有無logN*2 始点終点 + 反映logN
        - O(N + M+log(N))

    ... あれ？無作為にデータが与えられた場合、ソートに時間使うんじゃね？？
    """
    N,M, Sx, Sy = map(int, input().split())
    row_house_map, col_house_map = dict(), dict
    for i in range(N) :
        X, Y = map(int, input().split())
        try :
            row_house_map[Y].append(X)
        except KeyError :
            row_house_map[Y] = []
            row_house_map[Y].append(X)
        except Exception as e :
            raise e
        try :
            col_house_map[X].append(Y)
        except KeyError :
            col_house_map[X] = []
            col_house_map[X].append(Y)
        except Exception as e:
            raise e
    
    
    
    result = 0
    for _ in range(M) :
        d, c = input().split()
        c = int(c)
        query = []
        if d == "D" or d=="U" :
            try :
                if len(row_house_map[Sy]) == 0 :
                    row_house_map[10**10].append(1)

                if d == "D" :
                    e = bisect.bisect(row_house_map[Sy], Sx)
                    s = bisect.bisect_left(row_house_map[Sy], Sx+c)
                    for k in range(s,e) :
                        if Sx<=row_house_map[Sy][k]<=Sx+c :
                            query.append([Sy,row_house_map[Sy][k]])
                    for que in query :
                        pass
            except KeyError :
                #調査する必要なし。修了。
                pass
            else :
                pass

            get_house = []

            Sx += c
        else :
            Sy += c
    
    return

from sortedcontainers import SortedSet
def main2() :
    """ sortedSetを使ってみようの会 """
    pass

if __name__ == "__main__" :
    #main()
    check()
