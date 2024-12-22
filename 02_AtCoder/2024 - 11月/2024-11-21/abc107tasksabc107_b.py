""" #####################################################
発想

- H,W行の全部白を除く。
- HxW <= 10**4
- 全数調査
    - 行(横方向が全部白か)を調査して、削除処理=HxW
    - 列(縦方向が全部白か)を調査して、削除処理=HxW
    - よって計算量は O(HxW + HxW) となり高速だろう

##################################################### """
def check() :
    return


def main() :
    H, W = map(int, input().split())
    delH_grid = []
    del_count_col = 0
    for i in range(H) :
        tmp = input()
        for j in range(W) :
            if tmp[j] == "#" :
                break
        else :
            del_count_col += 1
            continue #リストを追加しない
        delH_grid.append(list(tmp))
    
    results = [[] for i in range(H-del_count_col) ]
    for j in range(W) :
        for i in range(H-del_count_col) :
            if delH_grid[i][j] == "#" :
                break
        else :
            continue
        for i in range(H-del_count_col) :
            results[i].append(delH_grid[i][j])
    
    for i in range(H-del_count_col) :
        print("".join(results[i]))
    return


if __name__ == "__main__" :
    main()
    #check()
