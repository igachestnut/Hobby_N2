""" #####################################################
発想


##################################################### """
from bisect import bisect
def cheaker() :
    a = list(range(0, 10, 3))
    j = bisect(a, 4.5)
    result = a.pop(j)
    result2 = a.pop(j-1)
    print(j, result, result2)
    return


def main2() :
    """ bisectを用いた導出 """
    H, W, Q = map(int, input().split())
    col_wall_map = [None] + [[j for j in range(1, W+1)] for i in range(H)] #入力が1~H であるため、入力に合わせて0を追加する。
    row_wall_map = [None] + [[i for i in range(1, H+1)] for j in range(W)]

    #print(col_wall_map)
    #print("----------------------")
    #print(row_wall_map)
    #print("----------------------")
    
    for q in range(Q) :
        R, C = map(int, input().split()) #R=たてにおける行数の位置, C=横の何要素目か 
        
        #配列の要素を確認する。
        if len(col_wall_map[R]) == 0 and len(row_wall_map[C]) : continue #既に壁は存在しない為抜き出し調査する必要なし
        elif len(col_wall_map[R]) == 0 and len(row_wall_map[C]) == 1 : #row(上下探索)だが、要素が確定している。
            only_num = row_wall_map[C].pop()
            j = bisect(row_wall_map[only_num], R)
            col_wall_map[only_num].pop(j-1)
        elif len(col_wall_map[R]) == 0 : #row(上下探索)だけを調査して終了
            # 上下探索 : 同じ要素が存在しないバージョン。
            j = bisect(row_wall_map[C], R) 
            if j == 0 : #挿入位置が頭かつ、同じ数字が存在しないと判断された場合。上だけ削除する。
                row_wall_map[C].pop(0) 
            elif j == len(row_wall_map[C]) -1 :#最後尾だった場合
                row_wall_map[C].pop() 
            else :
                row_wall_map[C].pop(j)
                row_wall_map[C].pop(j-1) 
        elif len(row_wall_map[C]) == 0 and len(col_wall_map[R]) == 1: #col(左右探索)だけして終了だが、左右の抜き出す要素が確定している。
            only_num = col_wall_map[R].pop()
            j = bisect(col_wall_map[only_num], C)
            row_wall_map[only_num].pop(j-1)
        elif len(row_wall_map[C]) == 0 : #col(左右探索)だけして終了
            # 左右探索 : 同じ要素が存在しないバージョン。
            i = bisect(col_wall_map[R], C) 
            if i == 0 : #挿入位置が頭かつ、同じ数字が存在しないと判断された場合。上だけ削除する。
                col_wall_map[R].pop(0) 
            elif i == len(col_wall_map[R]) -1 :#最後尾だった場合
                col_wall_map[R].pop() 
            else :
                col_wall_map[R].pop(i)
                col_wall_map[R].pop(i-1)
        else : #上下探索・左右探索が必要 かつ (R, C)が壁上を指している可能性がある場合。
            # 上下探索 (一応(R,C)に壁の有無を確認)
            j = bisect(row_wall_map[C], R)
            if row_wall_map[j-1] == R : #同じ要素が存在した場合 同じ要素を抜き出して終了(左右は探索しない)
                i = bisect(col_wall_map[R], C)
                col_wall_map[R].pop(i-1)
                row_wall_map[C].pop(j-1)
                continue
            
            # 上下探索
            if len(row_wall_map[C]) == 1 : #上下探索において要素が一つしかない為確定抜き出し。
                only_num = row_wall_map[C].pop()
                j = bisect(row_wall_map[only_num], R)
                col_wall_map[only_num].pop(j-1)
            elif j == 0 : #挿入位置が頭かつ、同じ数字が存在しないと判断された場合。上だけ削除する。
                up_num = row_wall_map[C].pop(0) 
                i = bisect(col_wall_map[up_num], C)
                col_wall_map[up_num].pop(i-1)
            elif j == len(row_wall_map[C]) -1 :#最後尾だった場合
                down_num = row_wall_map[C].pop() 
                i = bisect(col_wall_map[down_num], C)
                col_wall_map[down_num].pop(i-1)
            else : #中央位置が存在する場合
                up_num = row_wall_map[C].pop(j)
                down_num = row_wall_map[C].pop(j-1) 
                i = bisect(col_wall_map[up_num], C)
                col_wall_map[up_num].pop(i-1)
                i = bisect(col_wall_map[down_num], C)
                col_wall_map[down_num].pop(i-1)
            
            # 左右探索:同じ要素存在しない。
            i = bisect(col_wall_map[R], C)   
            if len(row_wall_map[C]) == 0 and len(col_wall_map[R]) == 1: #左右の要素が一つで抜き出す要素が確定している。
                only_num = col_wall_map[R].pop()
                j = bisect(col_wall_map[only_num], C)
                row_wall_map[only_num].pop(j-1)        
            elif i == 0 : #挿入位置が頭かつ、同じ数字が存在しないと判断された場合。右だけ削除する。
                right_num = col_wall_map[R].pop(0) 
                j = bisect(row_wall_map[right_num], R)
                row_wall_map[right_num].pop(j-1)
            elif i == len(col_wall_map[R]) -1 :#最後尾だった場合
                left_num = col_wall_map[R].pop() 
                j = bisect(row_wall_map[left_num], R)
                row_wall_map[left_num].pop(j-1)
            else : #中央位置が存在する場合
                print(col_wall_map[R])
                print(f"今回取り出すべき配列は、(R,C){R, C}")
                right_num = col_wall_map[R].pop(i)
                left_num = col_wall_map[R].pop(i-1) 
                j = bisect(row_wall_map[right_num], R)
                row_wall_map[right_num].pop(j-1)
                j = bisect(row_wall_map[left_num], R)
                row_wall_map[left_num].pop(j-1)
                
    result = 0
    for h in range(1, H+1) :
        result += len(col_wall_map[h])
    print(result)
    print("------------------------")
    print(col_wall_map)
    print(row_wall_map)
    return


if __name__ == "__main__" :
    main2()
    #cheaker()
