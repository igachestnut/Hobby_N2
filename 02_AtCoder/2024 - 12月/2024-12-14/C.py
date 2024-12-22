def check() :
    return


def main() :
    """ 
    
    - 31人の参加 
    - 高い順番に得点を出力。

    - 全部の解き方を辞書順で全列挙.O(32)(bit全探索)
    - 順番の高い順にリストに入れる。
        - 現在におけるmax数値の取得 O(32) +
        - 小さい順からmaxと等しいのを見ていき該当するのを抜き出す。 O(32)

    ここで、辞書順に配列を列挙する方法
    - A, AB,AC,AD,AE, ABC, 
    - 10000, 
    - 11000, 10100, 10010, 10001
    - 11100, 11010, 11001, 10110, 10101, 10011,
    - 11110, 11101, 11011, 10111
    - 11111,
    - 01000, ...

    DP[0] = [[0,""]]
    DP[1] = [[0,""], [a,"A"]]
    DP[2] = [[0,""], [a,"A"], [b,"B"], [a+b,"AB"]]
    sum(2718*5) < 2* 10**4

    
    """
    score = list(map(int, input().split()))
    score_alphabet = ["A","B","C","D","E"]
    DP = [[[] for j in range(sum(score)+1)] for i in range(6)]
    DP[0][0].append("")
    for i in range(5) :
        for j in range(len(DP[i])) :
            for k, s in enumerate(DP[i][j]) :
                DP[i+1][j].append(s)
                DP[i+1][j+score[i]].append(s+score_alphabet[i])

    for j in range(len(DP[-1])-1, -1, -1) :
        if DP[5][j] != [] :
            DP[5][j].sort()
            for k,s in enumerate(DP[5][j]) :
                print(s)
    return


if __name__ == "__main__" :
    main()
    #check()
