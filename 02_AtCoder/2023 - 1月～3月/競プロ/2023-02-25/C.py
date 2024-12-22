


def memo() :
    """
時間内に解けなかった問題
set使って、座標値の比較をすれば勝ちでした
    """





def cheaker() :
    import numpy as np
    a = np.array([1,0])
    b = np.array([1,0])
    print(a+b)
    return

def move(Str):
    if Str == "R" :
        return [0,1]
    elif Str == "L" :
        return [0,-1]
    elif Str == "U" :
        return [-1,0]
    else :
        return [1,0]

def main() :
    N = int(input())
    S = input()

    dist = [[0 for _ in range(N)] for i in range(N)]
    #最初にいる座標と、そこをTrueにする。
    x,y = 0,0
    dist[x][y] = True#記入
    
    for i in range(N) :
        point = move(S[i])
        x,y = x + point[0], y + point[1]
        if dist[x][y] :
            print("Yes")
            return 
        else :
            dist[x][y] = True 
    print("No")
    return

def move2(dist,Str) :
    if Str == "R" :
        dist[0] += 1
        return dist
    elif Str == "L" :
        dist[1] += 1
        return dist
    elif Str == "U" :
        dist[2] += 1
        return dist
    else :
        dist[3] += 1
        return dist
    
def main2():
    N = int(input())
    S = input()
    dist = [0 for i in range(4)]
    for n in range(N):
        if (dist[0] or dist[1]) and (dist[2] or dist[3]):
            if dist[0] == dist[1] and dist[2] == dist[3] :
                print("Yes")
                return 
        dist = move2(dist,S[n])
    print("No")
    return

if __name__ == "__main__" :
    main2()
    #cheaker()
