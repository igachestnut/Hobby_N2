""" #####################################################
発想

リーダーの向き変更の最小
E = 東 = 右向き
W = 西 = 左向き
EExWWW が良き

Case
- 一番左がリーダー →2~N まで全員左向き (N-2)-Wの数
- 中央がリーダー →1~i-1 まで右向き (i-1)-Eの数 + i+1~Nまで左向き(N-(i+1))-Wの数
- 一番右がリーダー →1~N-1 まで全員右向き (N-1-1)-Eの数 

よって、1~i~N について、直さなければならない数というのは、
iより左に位置する Wの数+ iより右に位置するEの数の総数
dbの総数を定義したうえで、


1. 全体総数計算
2. 

##################################################### """
def check() :
    return


def main() :
    N = int(input())
    S = input()
    EW_counts = [0, 0]
    for s in S:
        if s == "E": EW_counts[0] += 1
        else: EW_counts[1] += 1
    
    # 集合Nにおけるi=1の時の状態
    if S[0] == "E" :
        result = EW_counts[0]-1
    else :
        result = EW_counts[0]
    
    tmp_result = EW_counts[0]
    for i in range(1, N) :
        if S[i] == "E" :
            tmp_result -=1
        if S[i-1] == "W" :
            tmp_result += 1 
        result = min(result, tmp_result)
    print(result)
    return

def main() :
    """ 1~Nまで遷移させて計算する方法

    1. i=1におけるEの数え上げ
    2. 2~N まで以下の実行. (2~Nまで向きなおす量を計算)
        1. iの要素を確認、向きなおす必要があったEだった場合、向きなおす必要がなくなるので、値を減らす
        2. i-1の要素を確認、向き直す必要のある人Wがいたら、値を加算する
    """
    N = int(input())
    S = input()
    E_count = 0
    for i in range(1, N):
        if S[i] == "E": E_count+=1

    result = E_count
    tmp_result = E_count
    for i in range(1, N) :
        if S[i] == "E" :
            tmp_result -=1
        if S[i-1] == "W" :
            tmp_result += 1 
        result = min(result, tmp_result)
    print(result)
    return

if __name__ == "__main__" :
    main()
    #check()
