""" ########################################
MEMO

#周りの自由度1の記載
if h-1 < 0 : #上がマップ外
    pass
else :
    score_map[h-1][w] = 1 if not score_map[h-1][w] else score_map[h-1][w] #既に調査済みなら(磁石ならそのまま)

について

if 0 == ---
    まだ調査していないよ！そのまま返す
    
    他には
    1(自由度)が代入されている場合と、
    -1(磁石そのもの)が代入されている場合がある。
    それはそのまんまでいいので、ということ。



"""


def cheaker() :
    return


def main() :
    H, W = map(int, input().split())
    """
    S = []
    for h in range(H) :
        S.append(list(input()))
    """ 
    # 最大自由度をメモする、空の領域の作成(初期化としては値は0)
    score_map = [[0 for w in range(W)] for h in range(H)]
    
    # まず、の場所を-1に、磁石の上下を1にする。O(4N)処理=O(N) 
    for h in range(H) :
        s = list(input())
        for w in range(W) :
            if s[w] == "#" :
                #磁石位置の記載
                score_map[h][w] = -1
                #周りの自由度1の記載
                if h-1 < 0 : #上がマップ外
                    pass
                else :
                    score_map[h-1][w] = 1 if 0 == score_map[h-1][w] else score_map[h-1][w] #既に調査済みなら(磁石ならそのまま)
                if w-1 < 0 : #左がマップ外
                    pass
                else :
                    score_map[h][w-1] = 1 if 0 == score_map[h][w-1] else score_map[h][w-1] #既に調査済みなら(磁石ならそのまま)
                if h+1 >= H : #下がマップ外
                    pass
                else :
                    score_map[h+1][w] = 1
                if w+1 >= W : #右がマップ外
                    pass
                else :
                    score_map[h][w+1] = 1
                    
    
    # 作成した配列を左上から全調査して、最大数を求める。
    # 既に値が代入されている場合は調査しなくてもよいのでスルーする。
    # ある点が何もなく自由に動ける場合、BFSで自由に行ける領域を全調査する。(setでindexを追加する)
    # 調査が終了したら、その最大lenをその調査した場所に全代入する
    for hi in range(H) :
        for wj in range(W) :
            #既にメモされている場合→終了
            if score_map[hi][wj] != 0 :
                continue
            
            #動ける領域の調査開始 BFSの準備
            queue = []            #調査する場所
            roming_aria = set([]) #自由に動ける場所の結果
            write_aria  = set([]) #結果を記入する場所
            queue.append([hi, wj])
            score_map[hi][wj] = 1 #一度調査済みの意
            roming_aria.add((hi, wj))
            write_aria.add((hi, wj))
            
            # BFS
            while queue :
                que = queue.pop()
                i, j = que[0], que[1]
                # 上の調査
                if i-1 < 0 : #上がマップ外
                    pass
                else :
                    if 0 == score_map[i-1][j] :   #未調査
                        queue.append([i-1, j])    #調査領域の追加
                        score_map[i-1][j] = 1     #一度調査済みの意
                        roming_aria.add((i-1, j)) #行ける場所の追加
                        write_aria.add((i-1, j))  #結果を記入する場所の追加
                        
                    elif 1 == score_map[i-1][j] : #調査済み
                        roming_aria.add((i-1, j)) #行ける場所の追加
                    else :
                        print("変なことが発生しています")
                    
                    
            
                # 左の調査
                if j-1 < 0 : #左がマップ外
                    pass
                else :
                    if 0 == score_map[i][j-1] :   #未調査
                        queue.append([i, j-1])    #調査領域の追加
                        score_map[i][j-1] = 1     #一度調査済みの意
                        roming_aria.add((i, j-1)) #行ける場所の追加
                        write_aria.add((i, j-1))  #結果を記入する場の追加
                        
                    elif 1 == score_map[i][j-1] : #調査済み
                        roming_aria.add((i, j-1)) #行ける場所の追加
                    else :
                        print("変なことが発生しています")
                        
                # 右の調査
                if i+1 >= H : #下がマップ外
                    pass
                else :
                    if 0 == score_map[i+1][j] :   #未調査
                        queue.append([i+1, j])    #調査領域の追加
                        score_map[i+1][j] = 1     #一度調査済みの意
                        roming_aria.add((i+1, j)) #行ける場所の追加
                        write_aria.add((i+1, j))  #結果を記入する場所の追加
                        
                    elif 1 == score_map[i+1][j] : #調査済み
                        roming_aria.add((i+1, j)) #行ける場所の追加
                    else :
                        print("変なことが発生しています")
                
                # 下の調査
                if j+1 >= W : #右がマップ外
                    pass
                else :
                    if 0 == score_map[i][j+1] :   #未調査
                        queue.append([i, j+1])    #調査領域の追加
                        score_map[i][j+1] = 1     #一度調査済みの意
                        roming_aria.add((i, j+1)) #行ける場所の追加
                        write_aria.add((i, j+1))  #結果を記入する場所の追加
                        
                    elif 1 == score_map[i][j+1] : #調査済み
                        roming_aria.add((i, j+1)) #行ける場所の追加
                    else :
                        print("変なことが発生しています")

            # 調査結果、動ける領域の最大値
            Free_result = len(roming_aria)
            for i, j in write_aria : #結果の記入
                score_map[i][j] = Free_result
                
            
    #print(score_map)
    h_Max = [max(l) for l in score_map]
    print(max(h_Max))
    
    return



if __name__ == "__main__" :
    main()
    #cheaker()
