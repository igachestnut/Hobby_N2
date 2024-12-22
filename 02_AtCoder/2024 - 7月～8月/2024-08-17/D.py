""" これだとアウト

2→8、2→9を検知した後に、

4→2を検知すると、無駄に
4→9はうまくいかないのに、4→2→9は旨く行く判定となってしまい、問題とは間違っている。ことになる。

あと、O(N^2)ね。
どうやってうまくいかない場合でも取得できるようにしたか。



"""
def cheaker() :
    return


def main() :
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    results = [-1 for i in range(N)] #node i における、到達可能点の数をメモするリスト
    for i in range(N) :
        tmp_result = 0
        tmp_dis = 0
        # Noneiから時計回りに行けるNodeへ全調査する。
        for j in range(i, N+i-1) :
            mod_j = j % N
            tmp_dis += A[mod_j]
            if tmp_dis % M == 0 :#距離が倍数条件に合致した場合
                print(f"{i+1}→{(mod_j+2)%N}を検知しました")
                tmp_result += 1
                #到達したNodeの計算が終了しているかどうか確認し、到達済みなら終了する。
                t = (mod_j +1) % N
                if results[t] >= 0 :
                    results[i] = results[t] + tmp_result
                    break
        if results[i] == -1 :
            print(f"{i+1}indexにおいて、他に計算した経歴が存在しない為、そのまま加算して終了することにしました。")
            results[i] = tmp_result
        print(results)
    
    print(sum(results))
    return


if __name__ == "__main__" :
    main()
    #cheaker()
