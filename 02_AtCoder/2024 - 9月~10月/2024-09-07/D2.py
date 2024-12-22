def cheaker() :
    return


def main() :
    H, W, Q = map(int, input().split())
    floor = [[-1 for i in range(W+2)]]
    for i in range(H) :
        floor.append([-1] + [1 for _ in range(W)] + [-1])
    floor.append([-1 for i in range(W+2)])
    #print(floor)
    #print(len(floor))
    #print(len(floor[0]))
    
    for q in range(Q) :
        R, C = map(int, input().split())
        #print(R, C)
        if floor[R][C] == 1 :
            floor[R][C] = 0
        else :
            #上調査
            u = 1
            while floor[R-u][C] == 0 : u += 1
            if floor[R-u][C] == -1 : pass
            else : floor[R-u][C] = 0
            
            #下調査
            d = 1
            while floor[R+d][C] == 0 : d += 1
            if floor[R+d][C] == -1 : pass
            else : floor[R+d][C] = 0
            
            #左調査
            l = 1
            while floor[R][C-l] == 0 : l += 1
            if floor[R][C-l] == -1 : pass
            else : floor[R][C-l] = 0
            
            #右調査
            r = 1
            while floor[R][C+r] == 0 : r += 1
            if floor[R][C+r] == -1 : pass
            else : floor[R][C+r] = 0
                
    result = 0
    for h in range(1, H+1) :
        for j in range(1, W+1) :
            result += floor[h][j]
    print(result)
    for i in range(len(floor)) :
        print(floor[i])    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
