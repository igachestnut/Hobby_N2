""" 高橋君の嘘をみぬけ！な問題

N を構成する
[1000円枚数, 5000円枚数, 10000円枚数]は存在する?

- Y<2*10**7 
- Yを構成する最低枚数
    - yukiti = Y//10000 
    - higuti = (Y-yukiti*10000 )//5000
    - noguti = ...
- Yを構成する最大枚数
    - noguti = y//1000

- 10h を表現する方法
    - 10 or 6 or 2 or 1
- 20h を表現する方法
    - 20 or 16 or 12 or 11 or 8 or 7 or 4 or 3 or 2
- 30h を表現する方法
    - 30 or 26 or 22 or 21 or 18 or 17 or 14 or 13 or 12 or ,,,,,,,,,
    - All, nog, hig, yuk 
    - 30 =  30,
    - 26 =  25,  1
    - 22 =  20,  2
    - 21 =  20,  0,   1
    - 18 =  15,  3,   0
    - 17 =  15,  1,   1
    - 14 =  10,  4,   0
    - 13 =  10,  2,   1
    - 12 =  10,  0,   2
    - 10 =   5,  5,   0
    -  9 =   5,  3,   1
    -  8 =   5,  1,   2
    -  6 =   0,  6,   0
    -  5 =   0,  4,   1
    -  4 =   0,  2,   2
    -  3 =   0,  0,   3
    ....なんとなくだが、
    最大枚数を順に定義していくとして、
    ある地点の最大枚数Aiとなったとき、次の処理としてnogutiを両替したら、それ以上の枚数の組み合わせは存在しない。
    1000 札を切り崩していって、5000を追加、5000円が2枚以上追加されたら、<2になるまでyukitiに変換する。
    という考え方。そして、新規に1000札を減らす際は、必ず5000円札の枚数を初期化するとか。
    - noguti とhiguti の枚数をあたりつけて2分探索し、最も近い範囲における調査をしていくって方法なら間に合いそう。
    つまり、樋口の枚数が0~最大数まで定義して、その時に考えられる枚数を全列挙、
    全列挙された中で一番近い上下を知り、上から樋口の枚数をずらしながらyukitiをプラスして、合計がそうなったらTrue、そうじゃないならFalseにする


- 10hの時の表現の種類 =4通り
    -20h の時 4*(4-1)//2 通り



...BFSとか?
- 最効率をやった→ダメでした、1回10000を両替して、1,2,6,10 の可能性を見る。...? 10**3 だけBFSにおける分岐点がある。


...逆に、N枚を使って表現できる、最も近い数値を調査する???
- もしN 枚を使用したときに考えられるすべての金額が定義できたら、
    - Nによってできる配列をAとすると、
    - log(A)　二分探索で導出することができそう。ではあるが。。そもそもAはどれくらいの長さになる...???それがわからない。

    

"""
def check() :
    return

import bisect
def main() :
    N, Y = map(int, input().split())
    max_noguti_count = Y//1000
    # 樋口一葉の枚数をindexとしたとき、残り野口だけで金額を表現したら何番目になるのかを列挙する
    bill_count = [max_noguti_count-i*5 +i for i in range(max_noguti_count//5+1)]
    bill_count.sort()
    print(bill_count)

    # 2分探索で最も近い場所を検索する
    candidate_higuti_count = bisect.bisect(bill_count, N) #indexがhigutiの枚数で、その時の数値が最も近い上側の総枚数となる。
    #print(bill_count[candidate_higuti_count])
    #print(candidate_higuti_count)

    # Nを下回るまで実施、上から可能性のある枚数をすべて列挙する。※野口は調査済みなので、固定するものとする。
    noguti_count, higukichi_count, yukichi_count = max_noguti_count-5*(len(bill_count)-candidate_higuti_count-1), len(bill_count)-candidate_higuti_count, 0
    while higukichi_count>1 and noguti_count + higukichi_count + yukichi_count > N :
        #print(noguti_count)
        #print(higukichi_count)
        #print(yukichi_count)
        yukichi_count += 1
        higukichi_count -=2

    #print(noguti_count, higukichi_count, yukichi_count)
    if noguti_count+higukichi_count+yukichi_count == N :
        print(noguti_count, higukichi_count, yukichi_count)
    else :
        print(-1, -1, -1)
    return


if __name__ == "__main__" :
    main()
    #check()
