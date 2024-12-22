""" #####################################################
発想

- 旅行が実現可能か調査する
- その場にとどまることはできない
    →偶奇性の観点より、
        t%2==0 の時、(x+y)%2==0 にしか到達できず
        t%1==0 の時、(x+y)%2==1 にしか到達できない。

- 上記の調査をすると、残りは、時間に間に合うかどうかを調査すればよいこととなる。
- tが決まっているため、時間に余裕を持たせることは考えなくてもよい
    - t_i1, t_i2 の時間で、sum(abs(x1-x2), abs(y1-y2)) が 
        t_2 - t_1 以内であるか調査すればよい

##################################################### """
def check() :
    return


def main() :
    N = int(input())
    time_sheet = []
    # 偶奇性から、到達可能か判断する。0,0出発である
    for i in range(N) :
        t, x, y = map(int, input().split())
        if t%2 != (x+y)%2 :
            print("No")
            return
        time_sheet.append([t, x, y])
    
    # 時間内に到達可能か判断する
    bt, bx, by = 0,0,0 #b→before_* の意味
    for i, [t,x,y] in enumerate(time_sheet) :
        if abs(t-bt) < abs(bx-x) + abs(by-y) :
            print("No")
            return
        bt, bx, by = t,x,y
    print("Yes")
    return


if __name__ == "__main__" :
    main()
    #check()
