""" 

flowをもう一度整理する。

1. 線の描画順序P を定義する。
2. 各Pに対して実行。
    1. Pのa,b or c,dに向けて時間入力、

"""
import math
import itertools
def checker() :
    N = int(input())
    n_parmutations = list(itertools.permutations(range(N)))
    print(n_parmutations)
    for p in n_parmutations :
        print(p)
        print(p[0])
    
    print()
    print(len(p))
    
    return


def main() :
    N, S, T = map(int, input().split())
    draw_points = [[0,0,0,0]] #描画の開始位置。[sx,sy, ex,ey]形式で入る
    for i in range(N) :
        sx,sy, ex,ey = map(int, input().split())
        draw_points.append([sx,sy, ex,ey])
    perm = list(itertools.permutations(range(N)))
    
    result = float("inf")

    for p in perm : #順列一つ一つに着目
        locus = [[0.0, 0,0]] #この順列において、経路(locus)の総距離と最終地点を記載するリスト。[distance, ex,ey]のようになっている
        for i in range(N) : #順列を一つ一つ実施
            new_locus = []
            for [total_distance, last_x, last_y] in locus :
                ln = p[i]+1 #ln = line_number の意味。 何番目の線を使用するか。 [1~N+1]である
                d1 = cal_dis(last_x, last_y, draw_points[ln][0], draw_points[ln][1])/S
                d2 = cal_dis(last_x, last_y, draw_points[ln][2], draw_points[ln][3])/S
                dt = cal_dis(draw_points[ln][0], draw_points[ln][1], draw_points[ln][2], draw_points[ln][3])/T
                new_locus.append([total_distance+d1+dt, draw_points[ln][2], draw_points[ln][3]])
                new_locus.append([total_distance+d2+dt, draw_points[ln][0], draw_points[ln][1]])
            #print(new_locus)
            locus = new_locus
        for i in range(len(locus)) : result = min(result, locus[i][0])
    print(result)
    return

def cal_dis(sx, sy, ex, ey) :
    """ 始点と終点を与えて、その距離を算出する関数 """
    return math.sqrt((ex-sx)**2 + (ey-sy)**2)


if __name__ == "__main__" :
    main()
    #checker()
