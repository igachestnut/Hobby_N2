def cheaker() :
    return


def main() :
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    
    distance = [-1 for i in range(N)] #結果の距離メモする場所
    
    queue_dict = {} #仮調査位置
    for n in range(N) :
        #調査位置を検査・距離の確定
        if P[n] in queue_dict.keys :
            dis = abs(n - queue_dict[P[n]])
            distance[n], distance[queue_dict[P[n]]] = dis, dis
            del queue_dict[P[n]]
        
        #調査位置の追加
        if P[n]+K < N : #調査したい高い数字がある位置
            high_num  = P[n]+1+K
            queue_dict[high_num] = n
        if P[n]-K > 0 : #調査したい低い数字がある位置
            lower_num = P[n]+1-K
            queue_dict[lower_num] = n
            
        
    # sortしたdict情報の作成(indexの順番で、)
    dict_of_sorted_P = {}
    for n in range(N) :
        dict_of_sorted_P[P[n]] = n
    
    # これにより、調査したい位置と、その位置の距離が分かる。
    # あと最小を計算するだけ
    dis = N
    for i in range(N-K) : # 現在のPiと調査したいPiの値の比較⇒全体N-Kだけしか存在しない
        dis = min(dis, abs(dict_of_sorted_P[i]-dict_of_sorted_P[i+K]))
        
    
        
    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
