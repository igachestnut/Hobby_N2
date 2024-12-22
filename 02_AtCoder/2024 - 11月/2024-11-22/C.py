def check() :
    return


def main() :
    """ 発想
    
    - 111/222 を見つけるプログラム
    - このままでは条件分岐がめんどいので、1112333を見つけるプログラムにしましょう。
        - if before_s > S[i] の時、不正な値が入力されたということなので、現時点の最大数を計算して終了する。
            - 現時点の最大数を出すプログラム
            → [x, 1, y]の形式であること。(s_count[1] != 1の時、答えは0である)
            → result = max(result, min(x,y)*2+1)
    """
    N = int(input())
    S = input()

    # 文字列を抜き出せるだけ抜き出して、その時の最大数を計算する
    result = 0
    tmp_str_counts = [0,0,0]
    i = 0
    while i < N :
        if S[i] == "1" :
            if tmp_str_counts[1] == 0 and tmp_str_counts[2] == 0 :
                tmp_str_counts[0] += 1
            else : #計算を終了し、最大数をメモる
                result = max(result, get_result(tmp_str_counts))
                tmp_str_counts = [1,0,0]

        elif S[i] == "/" :
            if tmp_str_counts[2] == 0 and tmp_str_counts[1] == 0 :
                tmp_str_counts[1] += 1
            else :#不正な値が入ったら終了する。
                result = max(result, get_result(tmp_str_counts))
                tmp_str_counts = [0,1,0]
        else :
            if tmp_str_counts[1] != 1 :
                result = max(result, get_result(tmp_str_counts))
                tmp_str_counts = [0,0,0]
            else :
                tmp_str_counts[2] += 1
        i+=1
        #print(tmp_str_counts)
    result = max(result, get_result(tmp_str_counts))
    print(result)
    return

def get_result(counts:list) :
    """ 与えられた[x,1,y]形式の数字における最大数を返すプログラム """
    if counts[1] != 1 :
        return 0
    return min(counts[0],counts[2])*2+1


if __name__ == "__main__" :
    main()
    #check()
