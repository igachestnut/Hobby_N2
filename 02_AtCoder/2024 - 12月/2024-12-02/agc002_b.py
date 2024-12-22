""" #####################################################
発想

- 赤いボールが入っている可能性がある箱数の導出。
    - 赤いボールが入っているor(入っている可能性がある)iをaiとする。
    - 初期条件 ai=1 で、N[i] = 1の時、
        - ボールは必ず移動する。
    - N[i] = 2の時、
        - ボールは移動しない可能性もあるし、移動する可能性がある。
        - →ボールの入っている可能性がある箱の総数は2個となる。
    - N[i] に赤いボールがあるとき、すんごく強い染色ナタメ、中に入っている白ボールを赤く染色すると思うとわかりやすいかも。

- 必要な情報
    - ある地点i に何個ボールが入っているか。
    - ある地点i は赤いか否か。
##################################################### """
def check() :
    return


def main() :
    N,M = map(int, input().split())
    boxes = [1] * (N+1)
    isRed = [False] *(N+1)
    isRed[1] = True

    for i in range(M) :
        x,y = map(int, input().split())
        if isRed[x] :
            isRed[y] = True
            boxes[y] += 1
            boxes[x] -= 1
            if boxes[x] == 0 :
                isRed[x] = False
        else :
            boxes[y] += 1
            boxes[x] -= 1
    print(sum(isRed))
    return


if __name__ == "__main__" :
    main()
    #check()
