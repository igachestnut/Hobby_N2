""" ##################################################
入力
    N : Pの長さ
    K : 添字の重さ (i, i+Kで構成されるindexが良い添字)
    P : 適当に並べられた1~Nの配列

発想
    (1) 添え字の数
        良い添字は、必ずi, i+(K-1)で構成.注意:K自体は連続数の種類数 ⇒K=3 1,2,3で終わり iが1ならK-1まで
        つまり、配列Nの中に、添字自体はN-Kだけ存在する。
        O(N)
    
    (2) 方法
        Pを位置を記憶した状態でsort = dict_Pとする
        (dictでメモ)
        
        dict_Pをi~N-Kまで調査して、最小値を計算する
        O(N)
        
結論
    どうやら間違いっぽい。
    ⇒問題文の理解が足りていない。
    
    間違っていた点
    調査する領域を最初と最後ではなく、
    最初から最後のindexが該当する場所の最大len()ということ
    
    つまり
    a,a+K-1の2つlen(最大index-最小index)ではなく、
    a,a+1,,,a+K-1 に存在するすべてのindexのlen(最大index-最小index)
        
    ﾄｲｳｺﾄﾃﾞｽ。
    
    

考察
    なぜ理解できなかった？
    
    というか、
        ・N, P, i, aの状況をつなげるのに時間がかかりすぎてしまった。
        
        
自分の長所と短所？
    オブジェクトとして（図として）認知できるもの
    に対しては、処理量の把握もしやすい。
    
    逆にできないことに対して
    (数学的根拠のみによって定義される問題)はきついものがある。
    

本気で点数を取りに行く場合、
グラフ問題を優先して解くか？
解けるかどうかは置いておいて。（事故防止）
    
    
        
#################################################### """


def cheaker() :
    return



def main() :
    N, K = map(int, input().split())
    P = list(map(int, input().split()))      
    
    # 距離0の時だけ別出力
    if K < 1 :
        print("0")
        return      
        
    # sortしたdict情報の作成(indexの順番)
    dict_of_sorted_P = {}
    for n in range(N) :
        dict_of_sorted_P[P[n]] = n
        # dict_of_sorted_P[Nvalue] = そのNvalueがあった位置
    print(dict_of_sorted_P)
    
    # これにより、調査したい位置と、その位置の距離が分かる。
    # あと最小を計算するだけ
    dis = N
    for i in range(1, N-(K-1)) : # 全てのNvalueで良い添え字が存在する距離 の調査 (N-Kだけ)
        print(f"現在の調査Nvalue{i}")
        print(f"該当するPsortedのmin(i)位置P[Nvalue]{dict_of_sorted_P[i]}")
        print(f"該当するPsortedのmax(i+(K-1))位置P[Nvalue]{dict_of_sorted_P[i+(K-1)]}")
        
        dis = min(dis, abs(dict_of_sorted_P[i]-dict_of_sorted_P[i+(K-1)]))
        
    print(dis)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
