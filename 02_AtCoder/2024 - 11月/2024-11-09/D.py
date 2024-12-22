def check() :
    return

import bisect
def main() :
    """ 発想

    収穫の際にどれだけ簡単にH以上の長さの植物を見つけるのか?
    理想はO(1)で収穫すべき数の列挙をしたい。

    植えた総量を記載するデータ構造を作成する。
    bisectで位置を特定し、何とか導出する。
    """
    Q = int(input())
    
    plant_times = [[0, 0]] #カットされた時間とその量を記載する。
    now_time = 0 #現在の時間
    absolete_cut_count = 0 #カット済みの量を記載する
    for q in range(Q) :
        query = list(input())
        if query[0] == "1" :
            if plant_times[-1][0] == now_time :
                plant_times[-1][1] += 1
            else :
                plant_times.append([now_time, plant_times[-1][1]+1])
        elif query[0] == "2" :
            now_time += int(query[1])
        else :
            i = bisect.bisect_left(plant_times, [now_time-int(query[1]), float("-inf")], key=lambda x:x[0])
            result = plant_times[i][1] - absolete_cut_count
            print(result)
            absolete_cut_count = plant_times[i][1]
    return

def main2() :
    """ 発想

    収穫の際にどれだけ簡単にH以上の長さの植物を見つけるのか?
    理想はO(1)で収穫すべき数の列挙をしたい。

    植えられた時刻とそれ以上に存在するすべての植木鉢数を記入するデータ列を作る。
    [plants_tall, 累積]
    plants_tallをしたから順に実行していき、H以上の高さであるのを収穫
    """
    Q = int(input())
    
    plant_times = [[0, 0]] #カットされた時間とその量を記載する。
    pi = 0 #収穫済みの最終位置
    now_time = 0 #現在の時間
    absolete_cut_count = 0 #カット済みの量を記載する
    for q in range(Q) :
        query = list(map(int, input().split()))
        #print(query)
        if query[0] == 1 :
            plant_times.append([now_time, plant_times[-1][1]+1])                
        elif query[0] == 2 :
            now_time += int(query[1])
        else :
            # 着目している植物の高さ(素早さ) が 現在時刻-H よりも前なら(すでに植えられているなら)収穫できる
            while pi<len(plant_times)-1 and plant_times[pi+1][0] <= now_time-int(query[1]):
                pi += 1
            result = plant_times[pi][1] - absolete_cut_count #その地点で収穫できる総量-すでに収穫した量 = 新規に収穫する寮
            #print("-----------")
            #print(plant_times[pi][1] , absolete_cut_count)
            print(result)
            absolete_cut_count = plant_times[pi][1] #収穫済みの最終位置を記載する
    #print(plant_times)
    return


if __name__ == "__main__" :
    main2()
    #check()
