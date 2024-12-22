def cheaker() :
    return


def main() :
    """ 各Nodeの親は必ず一つである前提の上で成り立つ調査方法(Treeグラフよりいけそう) """
    N, K = map(int, input().split())
    tree = [-1 for i in range(N)]
    for i in range(N-1) :
        a, b = map(int, input().split())
        tree[b-1] = a-1
        
    V = list(map(int, input().split()))
    result_used_tree = [False for i in range(N)]
    for v in V :
        # 調査位置から上階へ使用する調査を行う。
        tmp_v = v-1 #0～n-1までの調査位置
        # 操作位置が-1(親が存在しない) or 既に調査済みまで 作業する。
        while tmp_v != -1 :
            if result_used_tree[tmp_v] : #使用済みであることが分かっている場合。
                break 
            result_used_tree[tmp_v] = True
            tmp_v = tree[tmp_v]  
    
    #print(result_used_tree)
    print(sum(result_used_tree))
    return

if __name__ == "__main__" :
    main()
    #cheaker()
