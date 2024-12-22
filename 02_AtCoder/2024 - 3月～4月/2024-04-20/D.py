def cheaker() :
    a = set([1,2,3])
    b = set([4,5,6])
    a.update(b)
    print(a)
    return


def main() :
    N, M = map(int, input().split())
    
    adjacency = [set() for n in range(N)] # 隣接リスト
    # 隣接リストの作成
    for m in range(M) :
        a, b = map(int, input().split())
        adjacency[a-1].add(b)
        adjacency[b-1].add(a)
        
    # 隣接リストより、孤立しているグループの計測
    Group_ID = [] # i = group数, j= そのグループに所属している人の番号
    Group_ID_num = 0
    IS_search = [False for n in range(N)] #調査済みかどうか判断する
    for i in range(N) : #調査の開始
        if IS_search[i] :
            continue
        
        # BFSの開始
        now_Group = set()        #現在の構成員
        now_Group.add(i+1)
        IS_search[i] = True    #その人は調査終了
        queue = set(adjacency[i]) #調査する場所の記載
        while queue :
            que = queue.pop() 
            if IS_search[que-1] :
                continue
            now_Group.add(que)
            IS_search[que-1] = True
            queue.update(list(adjacency[que-1]))
        
        #調査結果を保持
        Group_ID.append(now_Group)
        Group_ID_num += 1
    
    #print("現在わかる各配列のつながり状況は")
    #print(Group_ID)
    
    count = 0
    # 各グループにおいて足りない辺の算出
    for gn in range(Group_ID_num) : #グループナンバーだけ実行
        LEN = len(Group_ID[gn])
        #マックスの調査
        Max_friend = LEN * (LEN-1)
        
        #現在のつながり量の算出
        now_friend = 0
        for g in Group_ID[gn] :
            now_friend += len(adjacency[g-1])

        count += (Max_friend - now_friend) //2
        
    # 答えの出力
    print(count)
    
    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
