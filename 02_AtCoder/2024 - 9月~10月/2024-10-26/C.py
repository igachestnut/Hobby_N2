def check() :
    return


def main() :
    """ set型変数にデータを追加していって、残りのLENを調べる。

    マス目は、(i, j)だが、i*N + j形式の一つの変数として扱うこととする。 
    - ある駒からおけるか否かについて、
        - もし、j の値が-1 以下or N以上である、
        - もし、iの値が-1 or N以上であるとき、そのマスには何も置けない。
        それ以外は追加可能である。
    あと、ますが置かれている位置も置くことができないので、setに追加する。
    """
    N, M = map(int, input().split())

    blocked_positions = set()
    for m in range(M) :
        a, b = map(int, input().split())

        i, j = a-1, b-1
        blocked_positions.add(i*N+j)
        # そのマスの動かせる一を一つずつ確認する
        if 0<= i+2 < N :
            if 0<= j-1 < N : blocked_positions.add((i+2)*N +j-1)
            if 0<= j+1 < N : blocked_positions.add((i+2)*N +j+1)
        if 0<= i+1 < N :
            if 0<= j-2 < N : blocked_positions.add((i+1)*N +j-2)
            if 0<= j+2 < N : blocked_positions.add((i+1)*N +j+2)
        if 0<= i-1 < N :
            if 0<= j-2 < N : blocked_positions.add((i-1)*N +j-2)
            if 0<= j+2 < N : blocked_positions.add((i-1)*N +j+2)
        if 0<= i-2 < N :
            if 0<= j-1 < N : blocked_positions.add((i-2)*N +j-1)
            if 0<= j+1 < N : blocked_positions.add((i-2)*N +j+1)
    
    #print(blocked_positions)
    print(N**2 - len(blocked_positions))
    return


if __name__ == "__main__" :
    main()
    #check()
