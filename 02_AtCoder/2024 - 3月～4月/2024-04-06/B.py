import math

def cheaker() :
    return


def main() :
    N = int(input())
    position = []
    for i in range(N) :
        position.append(list(map(int, input().split())))
    
    
    for i in range(N) :
        max_C_num = 0
        max_distance = 0
        start_x, start_y = position[i][0], position[i][1]
        for j in range(N) :
            x, y = position[j][0], position[j][1]
            dis = math.sqrt((start_x - x) **2 + (start_y - y)**2)
            if dis > max_distance :
                max_distance = dis
                max_C_num = j
        
        #集計された番号は0～N-1であるため修正
        print(max_C_num+1)
        
    return


if __name__ == "__main__" :
    main()
    #cheaker()
