def cheaker() :
    return


def main() :
    N, A, B = map(int,input().split())
    P, Q, R, S = map(int,input().split())
    ans = [["." for j in range(S+1-R)] for i in range(Q+1-P)]
    
    #右斜め下黒線の記載。(i,j)において、i-jがA-Bと同値であることを利用する
    for i in range(Q+1-P) :
        for j in range(S+1-R) :
            if (P+i) - (R+j) == A-B : ans[i][j] = "#"
    
    #左斜め下黒線の記載。右上始点=(1, B+A-1)である。すると任意点=(k, B+A-k)である。このjに着目し、j がR以上S以下なら黒描画することになる。
    for k in range(P, Q+1) :
        #print(f"k{k}地点でのj の位置は{B+A-k}となっています。")
        if R <= B+A-k <= S : 
            ans[k-P][B+A-k-R] = "#" 

    #結果の出力
    for i in range(Q+1-P) :
        print("".join(ans[i]))
    return


if __name__ == "__main__" :
    main()
    #cheaker()
