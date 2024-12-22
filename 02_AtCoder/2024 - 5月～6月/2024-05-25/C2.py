def cheaker() :
    return


def main() :
    N, T = map(int, input().split())
    A = list(map(int, input().split()))

    #ビンゴするために残りの数を記したリスト
    number_of_remaining_columns = [N for n in range(N)] #列(縦)
    number_of_remaining_rows    = [N for n in range(N)] #行(横)
    number_of_remaining_right_diagonal = N #右斜め下に向かうビンゴ
    number_of_remaining_left_diagonal  = N #右斜め上に向かうビンゴ（左斜線）
    lef_max = N**2  #判定アルゴリズムだと、一番右下が入ってしまう為
    
    #ビンゴ状況を記載していく
    for i, Ai in enumerate(A) :
        x = (Ai-1)%N  #開けたいビンゴ表の列数
        y = (Ai-1)//N #開けたいビンゴ表の行数
        #print(f"{number_of_remaining_columns}column")
        #print(f"{number_of_remaining_rows}row")
        #print(f"right_dig{number_of_remaining_right_diagonal}")
        #print(f"left_dig{number_of_remaining_left_diagonal}")
        #縦
        number_of_remaining_columns[x] -= 1 
        if number_of_remaining_columns[x] == 0 :
            print(i+1)
            return
        #横
        number_of_remaining_rows[y] -= 1
        if number_of_remaining_rows[y] == 0 :
            print(i+1)
            return
        #斜め
        if (Ai-1) % (N+1) == 0 :
            number_of_remaining_right_diagonal -= 1
            if number_of_remaining_right_diagonal == 0 :
                print(i+1)
                return
        if (Ai-N) % (N-1) == 0 and Ai < lef_max:
            number_of_remaining_left_diagonal -= 1
            if number_of_remaining_left_diagonal == 0 :
                print(i+1)
                return
    
    print(-1)
    return
    
if __name__ == "__main__" :
    main()
    #cheaker()
