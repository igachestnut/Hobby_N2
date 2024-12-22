def cheaker() :
    return


def main() :
    H, W = map(int, input().split())
    S = list(map(int, input().split()))
    #S_input = list(input())
    #S = [int(s)-1 for s in S_input]
    S[0], S[1] = S[0]-1, S[1]-1
    map_C = [list(input()) for h in range(H)]
    X = list(input())
    for x in X :
        if x == "L" :
            walk = [0, -1]
        elif x == "R" :
            walk = [0, 1]
        elif x == "U" :
            walk = [-1, 0]
        else :
            walk = [1, 0]
        S = walk_S(S, walk, map_C, H, W)
    result_S = [s+1 for s in S]
    print(*result_S)
    return

def walk_S(S, walk, map, H, W) :
    """ マップを移動する関数
    
    Parameters
    -------------
    S : [int, int] 
        [i, j] 現在位置
    walk : [int, int]
        [i, j] 移動したい位置（Sからの相対位置）
    map : [[str,,,,]]
        マップ, H*W
    
    Return 
    ---------
    S : [int, int]
        次の開始位置
    """
    #マップ内か確認
    [sy, sx] = S
    [wy, wx] = walk
    if not (0 <= sy+wy < H) or not (0 <= sx+wx < W):
        return S
    
    #移動先に障害物があるか確認
    if map[sy+wy][sx+wx] == "#" :
        return S
    else :
        S = [sy+wy, sx+wx]
        return S


if __name__ == "__main__" :
    main()
    #cheaker()
