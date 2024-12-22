""" #####################################################
発想

- イルカの経路。2往復する。
- 同じ座標を複数通らないように移動しないといけない。
- 最短経路を一つ求めてね。

- -1000<= sx<tx <= 1000
- -1000<= sy<ty <= 1000

##################################################### """
def check() :
    sx,sy,tx,ty = map(int, input().split())
    result = 0
    result += (abs(sx-tx) + abs(sy-ty))*2
    result += (abs((sx-1)-(tx+1)) + abs((sy-1)-(ty+1)))*2
    print(result)
    print(len("UURDDLLUUURRDRDDDLLU"))
    return

def main() :
    sx,sy,tx,ty = map(int, input().split())
    result = ""
    X,Y = 0,0
    def go_left(): 
        X -= 1
        return "L"
    def go_right() :
        X += 1
        return "R"
    def go_down() :
        Y -= 1
        return "D"
    def go_up():
        Y += 1
        return "U"
    
    #移動調査の開始
    while X < tx : result += go_right()
    while Y < ty : result += go_up()
    while X > sx : result += go_left()
    while Y > sy : result += go_down()    

    result += go_down()
    while X < tx+1 : result += go_right()
    while Y < ty : result += go_up()
    result += go_left()
    result += go_up()
    while X > sx-1 : result += go_left()
    while Y > sy : result += go_down()
    result += go_right()

    print(result)
    return

def main2() :
    sx,sy,tx,ty = map(int, input().split())
    result = ""
    result += abs(sx-tx)*"R" + abs(sy-ty)*"U" + abs(sx-tx)*"L" + abs(sy-ty)*"D"
    result += "D"+ abs(sx-(tx+1))*"R" + abs(sy-1-ty)*"U" + "LU" + abs((sx-1)-tx)*"L" + abs(sy-(ty+1))*"D" + "R"
    print(result)

if __name__ == "__main__" :
    main2()
    #check()
