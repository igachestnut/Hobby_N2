def cheaker() :
    return


def main() :
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    #配列を整理する
    A.sort()
    B.sort()
    
    #追加したほうの配列を記入した変数
    tmp = -1 #A→0, B=1, 最初=-1
    
    #初期設定 aとbを調査位置へと持っていく
    if A[0] > B[0] : #最後に追加した数がaになりそう
        tmp = 0
    else :
        tmp = 1
    a, b = 1, 1
    
    #調査位置にて、追加したい方の数(小さいほう)を追加し続ける (両方比較でき続ける状態)
    while a < N and b < M :
        if A[a] < B[b] :
            if tmp == 0 :
                print("Yes")
                return
            tmp = 0
            a += 1
        else :
            tmp = 1
            b += 1
    
    #残った片方を調査。 Bのみなら存在しない
    if M-b > N-a :
        print("No")
        return
    else : #Aが残った場合
        pass
    
    # 現在の状況と配列の検査
    if (N-1)-a >= 1 :#残り要素が2つ以上ある場合(現在の調査位置と、配列の最後indexに差異がある)
        print("Yes")
        return
    elif tmp == 0 : #残っているのは1つだが、前回がa
        print("Yes")
        return
    else : 
        print("No")
        return
    
if __name__ == "__main__" :
    main()
    #cheaker()
