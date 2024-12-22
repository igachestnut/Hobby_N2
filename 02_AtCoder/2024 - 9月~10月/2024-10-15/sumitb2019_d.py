""" 便利配列を用いた探索

- 便利配列
N*10 の2次元リスト。Nは文字の数、10は現れる文字の種類数を示す。

現在着目しているindex = iとする。
iよりも後で、0~9の番号で最も左に現れるindexを格納する→を繰り返すとよいのでは?
"""

def checker() :
    return

def main() :
    N = int(input())
    S = input()

    # 番号i において、次のindexの位置を記載した便利配列の作成
    next_numbers = [[-1 for j in range(10)] for i in range(N+1)]
    for i in range(N, 0, -1) :
        for j in range(10): next_numbers[i-1][j] = next_numbers[i][j] #情報の引継ぎ。i=Nの時、これ以上文字列が存在しないため、ひとつ前も要素が存在しないとして記載している。
        next_numbers[i-1][int(S[i-1])] = i #現在着目しているS[i-1]において、番号sは新規に見つけた。見つけた位置i を最も早い位置として上書きする。
    
    # 数え上げの開始(3文字)
    result = 0
    for i in range(10) :
        s1 = next_numbers[0][i]
        if s1 == -1 : continue
        for j in range(10) :
            s2 = next_numbers[s1][j]
            if s2 == -1 : continue
            for k in range(10) :
                if next_numbers[s2][k] == -1 : continue
                else : 
                    #print(f"{i}{j}{k}:s1{s1},s2{s2},s3{next_numbers[s2][k]}")
                    result += 1
    print(result) 
    return





if __name__ == "__main__" :
    main()
    #checker()
