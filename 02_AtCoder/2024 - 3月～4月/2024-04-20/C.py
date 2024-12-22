def cheaker() :
    return


def main_all_search() : #N^2調査
    N = int(input())
    A = list(map(int, input().split()))
    
    #全数調査のやつ
    chenge_history = []
    for i in range(N) :
        now_sorted_num = i+1
        if A[i] != now_sorted_num :
            #jの特定
            for j in range(i+1, N) :
                #持ってきたい数字のゲット
                if A[j] == now_sorted_num :
                    break
            #変更処理
            A[i], A[j] = A[j], A[i]
            #変更履歴を残す 注意:indexは1~N+1
            chenge_history.append([i+1, j+1])
    
    #結果の出力
    print(len(chenge_history))
    for [i, j] in chenge_history :
        print(i, j)
            
    return

def main() : #計算数 (N)? 絶対に見た数値を正しい位置に持っていくことができるため
    """ 逆の考え方。
    
    現在発見したところに持っていく。
    情報更新する。という手法。
    現在の位置がOKになるまで実行する
    
    """
    N = int(input())
    A = list(map(int, input().split()))
    
    #結果用配列
    chenge_history = []
    
    #調査の開始
    i = 1 #1~N+1まで実行
    while i <= N :#配列が全て良くなるまで実行する。
        if A[i-1] == i : #現在注目している要素が大丈夫な場合→pass
            i += 1
            #print("現在の要素は善い状態です", i-1)
            continue
        #配列の交換(正しい位置に持っていく)
        #print("A[A[i-1]-1]",A[A[i-1]-1])
        #print("A[i-1]",A[i-1])
        a = i-1
        b = A[i-1]-1
        A[a], A[b] = A[b], A[a] #ex) A[i-1] = 3, A[A[i-1]-1] = A[3-1] = 1
        
        #print("現在の配列の状態は" , A)
        chenge_history.append([a+1, b+1])#注意：出力先のindexは1～N
        #input()
    
    #結果    
    K = len(chenge_history)
    print(K)
    for [i, j] in chenge_history :
        print(i, j)
    #print(A)

if __name__ == "__main__" :
    main()
    #cheaker()
