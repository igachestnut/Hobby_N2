"""

高橋(スライム)君の強さ出の最大
- 初期位置 (P,Q)が高橋君
- 隣接するスライムのうち、1/X 倍未満のものを選んで吸収。Sijだけ強さが増加


- 方針 見えるすべてのスライムを調査。(heapqに追加)
ただし、重複して追加することは避けたい。見えているか否かを配列で捜査すること
- heapq で抜き出し、OKなら作業。ダメだめなら修了
"""
def check() :
    return


import heapq
def main() :
    H,W,X = map(int, input().split())
    P,Q = map(int, input().split())
    S = []
    for i in range(H) :
        S.append(list(map(int, input().split())))

    is_show = [[True for j in range(W+2)]]
    for i in range(H) :
        is_show.append([True]+[False]*W+[True])
    is_show.append([True for j in range(W+2)]) 

    takahasi_S = S[P-1][Q-1]
    is_show[P][Q] = True
    query = [] #(s, [i,j]) スライムの強さ=s, 位置=i,jで作業する
    common_side = [(-1,0),(0,-1),(1,0),(0,1)] #上下左右
    for i,j in common_side :
        if is_show[P+i][Q+j] == False :
            query.append([S[P-1+i][Q-1+j], [P+i,Q+j]])
            is_show[P+i][Q+j] = True 
    heapq.heapify(query)

    # 調査の開始
    if query :
        q = heapq.heappop(query)
        while q[0] < takahasi_S/X :
            #print(f"現在着目しているのは{q}で、高橋君は{takahasi_S}で{takahasi_S/X}のスライムを取り込める")
            takahasi_S += S[q[1][0]-1][q[1][1]-1]
            for i,j in common_side :
                if is_show[q[1][0]+i][q[1][1]+j] == False :
                    heapq.heappush(query, [S[q[1][0]-1+i][q[1][1]-1+j], [q[1][0]+i,q[1][1]+j]])
                    is_show[q[1][0]+i][q[1][1]+j] = True 
            if query :
                q = heapq.heappop(query)
            else :
                q = [float("inf"), [-1,-1]]
    
    print(takahasi_S)
    return


if __name__ == "__main__" :
    main()
    #check()
