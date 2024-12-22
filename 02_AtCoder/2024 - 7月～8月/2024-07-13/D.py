

def cheaker() :
    return


def main() :
    """ グラフアルゴリズム　見えている辺orうえぃとの中で、一番軽いものを更新し続ける手法 """
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #行き先とWeightをまとめたリストを作成。
    #[[[3,2], [2,2]]] 第1Index＝現在の島 第二Index =その島から見えている辺の数 第三Index=[0]→見えている島、第三index=[1] = wight
    hen_map = [[] for n in range(N)]
    for i in range(M) :
        u, v, b = map(int, input().split())
        hen_map[u-1].append([v-1, b])
        hen_map(v-1).append([u-1, b])
    
    result_weight = [float("inf") for i in range(N)]
    result_weight[0] = 0
    
    queue = hen_map[0]
    while True :
        min_wight = float("inf")
        min_index = 0
        for que in queue :
            next_weight = que[1]+A[que[0]]
            result_weight[que[0]] = min(next_weight, result_weight[que[0]]) #行き先で最小値を見つける。
            if min_wight > next_weight :
                min_index = que[0] #次見えている位置を次の開始位置とする。
                
        queue.append(hen_map[min_index])
    
    
    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
