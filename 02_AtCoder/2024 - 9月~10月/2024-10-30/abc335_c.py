""" #####################################################
発想

パーツi の位置を出力したいのコーナー
ただ、正直なquery処理だと、N*Q回かかるので、TLEとなりそう。

すべての情報は追従することを利用するとよい。
P = [[0, 0] for i in range(N)] #すべてのパーツはこうている。

- 処理１が入力されたとき
    if que[1] == "R" : P.append([P[-1][0]+1, P[-1][1]])
    elif que[1] == "L" : P.append([P[-1][0]-1, P[-1][1]])
    elif que[1] == "U" : P.append([P[-1][0], P[-1][1]+1])
    else : P.append([P[-1][0], P[-1][1]-1])

- 現在の頭の位置 = P[-1]である。i=1の時
- つまりパーツi の時 =P[-i]でOK

##################################################### """
def check() :
    return


def main() :
    N, Q = map(int, input().split())
    P = [[i, 0] for i in range(N+1, 0, -1)]
    for q in range(Q) :
        que = list(input().split())
        if que[0] == "1" :
            if que[1] == "R" : P.append([P[-1][0]+1, P[-1][1]])
            elif que[1] == "L" : P.append([P[-1][0]-1, P[-1][1]])
            elif que[1] == "U" : P.append([P[-1][0], P[-1][1]+1])
            else : P.append([P[-1][0], P[-1][1]-1])
        else :
            print(*P[-int(que[1])])
    return


if __name__ == "__main__" :
    main()
    #check()
