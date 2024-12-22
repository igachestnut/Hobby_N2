""" 
発想

O(Q*M) で解く
edgeの作成、
最短距離順にedgeを作成。

- 問題時始め
    1. Questionの初期条件
    2. 到達可能なNodeの定義(まだ未到達のNodeの定義)
    3. 最短順にNodeをつなげていき、全てのNodeがつながったら終了する
    
- では、どのようにNodeをつなげるべきかつなげるべきでないか有無を判断する？
    - 問題から与えられる橋は離散的である。
    - 具体的には, 1-2-3  4-5 のように離散的である。
        この1-2-3~4-5をつなげる作業をしたいが、どのように判断すればよいかわからん。
        一応 1-2-3は任意のオブジェクト群ではある。
        親Nodeが分かるもしくは、その地点におけるつながっているNodeを保持できれば？？？
        [[1,2,3], [1,2,3], [1, 2, 3], [4, 5], [4, 5]]
        親を付けると、
        [[1,2,3], [-1, 1], [-1,1], [4,5], [-1, 4]]
        
        更にさらに、
        離散しているかどうかを判定するtmp_map 
        tmp_map = [None, None, ,,, ](N個だけ)
        与えられるB
        tmp_map = [0, 0, 0, 1, 1]
        tmp_edge = [[1,2,3], [4,5]]
        tmp_edge = {0:[1,2,3], 1:[4,5]}
        for m in range(M):
            #最短順につながりを検査
            v, t = saitan_map[m]
            if tmp_map[v-1] == -1 or tmp_map[t] == -1 : #離散しているNodeを検知した場合
                追加処理。もし両方とも新規Nodeなら新規Ｎｏｄｅ群を追加する。
                Map編集する
            elif tmp_map[v-1] == tmp_map[t-1] : #既につながっている場合
                continue
            else : #2つの別々のNode群を繋げれそうな場合。
                parent_edges = tmp_edge[v-1] 
                child_e = v-1 if tmp_map[v-1] != 0 else t-1
                for j in tmp_edge[t-1] : #つながり位置すべてに対して実行する。
                    tmp_map[j] = parent_edges
                del tmp_edge[t-1]
                
            もしすべてのＮｏｄｅで確認出来たら終了！
                
- 結論
間違いだった。
もしかしたら問題文で求めなければならない答えや、考慮すべきケースについて
不足があると思われる。
1. 各Nodeの最短距離を一筆書きをするイメージである。ただつながっていればよいわけではない。
2. 1が始点であり、Nが終点であること。N=3の場合で、1=3=2-3 (=は指定されている橋, -は最短距離を計算しなければならない経路)



それとは別に、
プログラムが思った通りの実装が行かなかった。
1. 最短順のマップを作成することは成功した
2. 多分Qiで与えられた初期条件から初期Node群の定義もできたはず
3. それ以降の処理がうまくいかん



"""
def cheaker() :
    return


def main() :
    N, M = map(int, input().split())
    dis = set()
    edges = []
    for i in range(M) :
        u, v, t = map(int, input().split())
        edges.append([u-1, v-1, t]) #u, v, t :u-Node1, v-Node2, t-距離 ※注意 u,vの番号は 0~N-1とする。 
        dis.add(t)
    
    # 最短距離順のedge_map作成
    shortest_order_edges = dict()
    for d in dis :
        shortest_order_edges[d] = []
    for i in range(M) :
        shortest_order_edges[edges[i][2]].append(edges[i][:2])
        
    print(shortest_order_edges)
        
    # 問題の解答はじめ
    Q = int(input())
    for q in range(Q) :
        K = int(input())
        B = list(map(int, input().split()))
        aria_num = [-1 for i in range(N)] #そのNodeにおける、Node群番号を格納するリスト
        aria = dict() #エリア。第1要素目にparentとなるエリアが格納される。それ以外は小Node
        aria_index = 0 #作成されたエリアの数。0がすべての親になる予定。
        process_count = 0 #エッジの確定回数。N-1だけ実行出来たら終了
        result = 0
          
        # 初期条件Bより、ariaの定義
        for b in B :
            [u, v, t] = edges[b-1] #注意bは1~Mである。リストの要素の指定するには-1すること
            if aria_num[u] == -1 and aria_num[v] == -1 : #両方未定義
                aria_num[u], aria_num[v] = aria_index, aria_index
                aria[aria_index] = [u, v]
                aria_index += 1         
            elif aria_num[u] == -1 : #左だけ未定義である場合、右のNode群にくっつける
                aria_num[u] = aria_num[v]
                aria[aria_num[u]].append(u)
            elif aria_num[v] == -1 :
                aria_num[v] = aria_num[u]
                aria[aria_num[v]].append(v)
            else :#両方とも定義済みである場合、小さいほうのNode群につなげる。
                if aria_num[u] < aria_num[v] : #もしu側の方が親だった場合
                    for a in aria[aria_num[v]] : #全てのエリア情報を上階に更新する。
                        aria_num[a] = aria_num[u]
                        aria[aria_num[u]].append(a)
                    aria[v] = [] #もう使わないエリアを更新する。
                elif aria_num[v] < aria_num[u] :
                    for a in aria[aria_num[u]] : #全てのエリア情報を上階に更新する。
                        aria_num[a] = aria_num[v]
                        aria[aria_num[v]].append(a) #エリアを引き継ぐ
                    aria[u] = [] #もう使わないエリアを更新する。
                else :#もし2つとも同じNode群だった場合。初期条件で必ず通らなければならない為resultをプラスするだけ。
                    process_count -= 1 #後続の処理で余分にプラスされてしまう為
            result += t #今回繋げたNode群を追加する。
            process_count += 1 #今回新しくNodeをつなげたため、+1する
            
        #print("貪欲法を開始します")
            
        #貪欲法を用いて、最短距離でかつ定義可能な辺を決定していく
        for t, tmp_edges in shortest_order_edges.items() :
            #print("////////////////////////////////")
            #print(f"t{t}")
            #print(f"tmp_edges{tmp_edges}")
            for u, v in tmp_edges :
                #2辺を使用するか否か判断し、結果に追加。
                if aria_num[u] == -1 and aria_num[v] == -1 : #両方未定義
                    aria_num[u], aria_num[v] = aria_index, aria_index
                    aria[aria_index] = [u, v]
                    aria_index += 1         
                elif aria_num[u] == -1 : #左だけ未定義である場合、右のNode群にくっつける
                    aria_num[u] = aria_num[v]
                    aria[aria_num[u]].append(u)
                elif aria_num[v] == -1 :
                    aria_num[v] = aria_num[u]
                    aria[aria_num[v]].append(v)
                else :#両方とも定義済みである場合、小さいほうのNode群につなげる。
                    if aria_num[u] < aria_num[v] : #もしu側の方が親だった場合
                        for a in aria[aria_num[v]] : #全てのエリア情報を上階に更新する。
                            aria_num[a] = aria_num[u]
                            aria[aria_num[u]].append(a)
                        aria[v] = [] #もう使わないエリアを更新する。
                    elif aria_num[v] < aria_num[u] :
                        for a in aria[aria_num[u]] : #全てのエリア情報を上階に更新する。
                            aria_num[a] = aria_num[v]
                            aria[aria_num[v]].append(a) #エリアを引き継ぐ
                        aria[u] = [] #もう使わないエリアを更新する。
                    else :#もし2つとも同じNode群だった場合。次のMに着目する
                        continue
                result += t #今回繋げたNode群を追加する。
                process_count += 1 #今回新しくNodeをつなげたため、+1する
                #print("-----------------")
                #print(aria_num)
                #print(aria)
                #print()
                
            if len(aria[0]) == N-1 : #parentとなるariaに全てのNodeが含まれたら終了する
                break                
        
        print(result)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
