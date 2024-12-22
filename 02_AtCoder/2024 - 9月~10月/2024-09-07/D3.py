""" #####################################################
発想

DB構造を工夫する。

1. 行から見て列の壁がある場所を格納したリスト。
2. 列から見て行の壁がある場所を格納したリスト。
この2つを作成。

左右の探索は1. 上下の探索は2. を使用して、破壊する位置を調査する。
それらを相互に反映させればよい！




##################################################### """
import bisect
def cheaker() :
    """ 2分探索の挙動を確かめる 
    
    どうやらどちらも入力されたindexの挿入を考えた際に一番適切な位置を返すようだ。
    すなわち、入力したいindexに最も近く、大きい値を出力する。4を挿入したい場合は、3の位置の次を出力する。
    
    bisect の戻り値 0~len(list) 挿入位置として入力すればよい数値を返してくれる。
    戻り値 0 : 該当する文字列は存在しない。それ以降の要素は全て挿入数字よりも高いもの。
    """
    a = [1,2,3,5,6,7]
    index = 8 #4に最も近い上下を調べるとして
    #print(bisect.bisect_left(a, index)) #下の値を調べる？
    print(bisect.bisect_right(a, index)) #上の値を調べる？
    
    
    
    return


def main() :
    H, W, Q = map(int, input().split())
    col_wall_map = [[None] + [j for j in range(1, W+1)] for i in range(H)] #入力が1~H であるため、入力に合わせて0を追加する。
    row_wall_map = [[None] + [i for i in range(1, H+1)] for j in range(W)]
    
    for q in range(Q) :
        R, C = map(int, input().split())
        
        #壁検索 : 2分探索を用いて、該当場所の壁の有無を確認
        j = binary_search(col_wall_map[R], C)
        if col_wall_map[R][j] == C :
            i = binary_search(row_wall_map[C], R)
            col_wall_map[R].pop(j)
            row_wall_map[C].pop(i)
            continue
        
        #上探索 : 2分探索を用いて、該当する列における、入力行の最も近い上下の値を見つけ出す。
        up_i = binary_search(row_wall_map[C], R)
        if up_i == None : pass #該当するindexが存在しない判定とされた場合。
        else : 
            up_j = binary_search(col_wall_map[C], R)
            row_wall_map[C].pop(up_i)
            col_wall_map[R].pop(up_j)
        
        
        #右探索 
        right_j = binary_search(col_wall_map[R], C)
        if right_j == None : pass #該当するindexが存在しない場合
        else :
            right_i = binary_search(row_wall_map[C], R)
            row_wall_map[C].pop(right_i)
            col_wall_map[R].pop(right_j)
            
            
        #right_i 
        #    col_wall_map.pop(R)
            
        

def binary_search(List, index, mode=1) :
    """ 与えられたindexに最も近い上の数値を探索し、そのindexを返す 
    
    Parameters 
    ----------
    - List : list
        検査するリスト
    - index : int
        判定したい文字列
    - mode : int
        0 or 1
        1 なら、indexより上部にある最も近いindexを返す。
        0 なら、indexより下部にある最も近いindexを返す。
        2 なら、両方tuple型で返す。
        
    Returns
    --------
    - int or tuple(int, int)
        modeが0,1ならint, 2ならtuple(int, int)
        取得するべきindexを返せるようになっている。
        もし該当するリストの要素が無い場合は Noneを返す。
        
    MEMO
    -----
    ねぇ。すべてOKの配列だった場合は
    OKとNGの関係をどう定義すればよいのむかつく 
    
    2分探索の特殊系ということが分かった。
    普通の2分探索は該当文字が挿入される位置を算出するものであるが、
    この場合、該当数字に最も近いleftとrightを導出したい。
    ErrorCaseとしては、配列が[0,1,2,3,4]の時、indexが4や5という最大以上を与えられた時。
    底を算出するのであれば、left+right //2 が一番左まで行ってくれているため算出可能だが、
    上の方が算出不可能である。
    
    というか、bitsetで要素を調べる。
    前後を調べる。
    該当すれば良き。該当なしなら終了で良くね？
    """
    if List == [] : return None
    
    left, right = 0, len(List)-1 #入力値のindexよりも大きく、最も小さい値
    while left != right-1 :
        tmp = (left + right) // 2
        if List[tmp] < index : left = tmp 
        else : right = tmp
    
    if mode == 1 :
        if right >= len(List) : return None
        else : return right
    elif mode == 0 :
        if left <= 0 : return None if List[0] > index else 0
        else : return left    
    else : 
        pass
    
def myfunc() :
    """ 入力された位置に壁が存在し、直接破壊をするのか否かを決めるfunction """
    pass


def main2() :
    """ bisectを用いた導出 """
    H, W, Q = map(int, input().split())
    col_wall_map = [[None] + [j for j in range(1, W+1)] for i in range(H)] #入力が1~H であるため、入力に合わせて0を追加する。
    row_wall_map = [[None] + [i for i in range(1, H+1)] for j in range(W)]
    
    for q in range(Q) :
        R, C = map(int, input().split()) #R=たてにおける行数の位置, C=横の何要素目か 
        
        #配列の要素を確認する。
        if len(col_wall_map[R]) == 0 and len(row_wall_map[C]) : continue #既に壁は存在しない為抜き出し調査する必要なし
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
            # 上下探索
            j = bisect(row_wall_map[C], R)             
            if row_wall_map[j-1] == R : #同じ要素が存在した場合 同じ要素を抜き出して終了(左右は探索しない)
                i = bisect(col_wall_map[R], C)
                col_wall_map[R].pop(i-1)
                row_wall_map[C].pop(j-1)
                continue
            elif j == 0 : #挿入位置が頭かつ、同じ数字が存在しないと判断された場合。上だけ削除する。
                up_num = row_wall_map[C].pop(0) 
                i = bisect(col_wall_map[R], up_num)
                col_wall_map[R].pop(i-1)
            elif j == len(row_wall_map[C]) -1 :#最後尾だった場合
                down_num = row_wall_map[C].pop() 
                i = bisect(col_wall_map[R], down_num)
                col_wall_map[R].pop(i-1)
            else : #中央位置が存在する場合
                up_num = row_wall_map[C].pop(j)
                down_num = row_wall_map[C].pop(j-1) 
                i = bisect(col_wall_map[R], up_num)
                col_wall_map[R].pop(i-1)
                i = bisect(col_wall_map[R], down_num)
                col_wall_map[R].pop(i-1)
            
            # 左右探索:同じ要素存在しない。
            j = bisect(col_wall_map[R], C)             
            if j == 0 : #挿入位置が頭かつ、同じ数字が存在しないと判断された場合。右だけ削除する。
                right_num = col_wall_map[R].pop(0) 
                i = bisect(row_wall_map[C], right_num)
                row_wall_map[C].pop(i-1)
            elif j == len(col_wall_map[R]) -1 :#最後尾だった場合
                left_num = col_wall_map[R].pop() 
                i = bisect(row_wall_map[C], left_num)
                row_wall_map[C].pop(i-1)
            else : #中央位置が存在する場合
                right_num = col_wall_map[R].pop(j)
                left_num = col_wall_map[R].pop(j-1) 
                i = bisect(row_wall_map[C], right_num)
                row_wall_map[C].pop(i-1)
                i = bisect(row_wall_map[C], left_num)
                row_wall_map[C].pop(i-1)
                
    result = 0
    for h in range(1, H+1) :
        result += len(col_wall_map[h])
    print(result)
    print(col_wall_map)
    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
