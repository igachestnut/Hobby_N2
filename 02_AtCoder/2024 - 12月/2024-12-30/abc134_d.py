""" #####################################################
発想

- i の倍数に書かれた箱に入っているボールの総数の余りがaiである

- 降順で考える。N~i~1 に遷移
1. iにおけるiの倍数の総和を調査する。
2. その値 ri != ai だった場合, その地点にボールを入れ、aiと同値にする。
後続の値がどのような数値を持っても、現時点で確定するための総和には変化が生じないため、値を確定して次へ行くことができる。

- 計算量O(N*ln(N))
    - 任意i における計算量 その地点における倍数の総和を調査するので、 N//i 回調査する。
    - これをN (N~1)まで実行するので、全体計算量は O(siguma_{i=N~i}(N//i))であり、これは O(N*siguma_{i=N~i}(1//i))となり右部分は調和級数であるため N*(ln(N)+γ) = N*(ln(N))となる



##################################################### """
def check() :
    return


def main() :
    N = int(input())
    A = [0] + list(map(int, input().split()))
    
    B = [] #結果: ボールを入れるindex 
    boxes = [0]*(N+1)
    for i in range(N, 0, -1) :
        tmp_sum = sum([boxes[j] for j in range(i, N+1, i)])
        if tmp_sum%2 != A[i] :
            boxes[i] = 1
            B.append(i)
    print(len(B))
    print(*B)
    return


if __name__ == "__main__" :
    main()
    #check()
