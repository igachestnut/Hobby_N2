""" #####################################################
発想


##################################################### """
def check() :
    return


def main() :
    H, W = map(int, input().split())
    Map = [[-1 for j in range(W+2)] for i in range(H+2)]
    # map情報を記入する
    for i in range(H) :
        S = list(input())
        for j, s in enumerate(S) :
            if s == "#": Map[i+1][j+1] = 1
            else: Map[i+1][j+1] = 0

    #print(Map)

    # 各マスの調査をする。
    #result = []
    for h in range(1, H+1) :
        tmp_strings = ""
        for w in range(1, W+1) :
            if Map[h][w] == 1 :
                tmp_strings += "#"
                continue

            count = 0
            _round = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 0),(0, 1),(1, -1),(1, 0),(1, 1)]
            for i, j in _round :
                if Map[h+i][w+j] == 1 : 
                    count += 1
            tmp_strings += str(count)
        print(tmp_strings)
        #result.append(tmp_strings)
    return


if __name__ == "__main__" :
    main()
    #check()
