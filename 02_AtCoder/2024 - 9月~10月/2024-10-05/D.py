
import math
import itertools


def checker() :
    N = int(input())
    comb = itertools.product(range(N), [0,1])
    print(list(comb))
    return


def main() :
    N, S, T = map(int, input().split())
    comb = itertools.combinations(range(N), N) #線の描画順序の全列挙

    drawing = [] #描画位置を保持するリスト。[a, b, c, d]
    for i in range(N) :
        a, b, c, d = map(int, input().split())
        drawing.append([a,b,c,d])

    result = float("inf")
    # 組み合わせ表より、全経路を検証し、その最短を知る。
    print(comb)
    for c in list(comb) : #全組み合わせ
        tmp_r = [0, 0, 0] #現在のそこまでの距離と、次の始点を記載するデータ。[dis, ex, ey]
        for i in range(N) :
            new_tmp_r = []
            tmp_t = (T/ cal_dis(drawing[c[i]-1][0], drawing[c[i]-1][1], drawing[c[i]-1][2], drawing[c[i]-1][3]))
            for tr in tmp_r :
                d1 = tr[0] + (S/cal_dis(tr[1], tr[2], drawing[c[i]-1][0], drawing[c[i]-1][1])) + tmp_t
                new_tmp_r.append([d1, drawing[c[i]][2], drawing[c[i]][3]])
                d2 = tr[0] + (S/cal_dis(tr[1], tr[2], drawing[c[i]-1][2], drawing[c[i]-1][3])) + tmp_t
                new_tmp_r.append([d2, drawing[c[i]][0], drawing[c[i]][1]])
            tmp_r = new_tmp_r
        for tr in tmp_r : result = min(result, tr[0])
    print(result)
    return

def cal_dis(sx, sy, ex, ey) :
    """ 始点と終点を与えて、その距離を算出する関数 """
    return math.sqrt((ex-sx)**2 + (ey-sy)**2)


if __name__ == "__main__" :
    #main()
    checker()
