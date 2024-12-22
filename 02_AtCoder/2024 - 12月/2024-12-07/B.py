""" 
加湿される床の最大マス数を求める。

加湿器の位置をKとすると
..K..
.....
.....

D=3 のとき
23K32
12321
01210
Kからのきょりがですね

H,W が<10 
2個だけ加湿器を置ける

1マス置いたときの全体計算量は,100
これをi,j をそれぞれ1~100 固定して考えるとすると
O(HW **3) 10**2**3 = 10**6 で間に合う


では、マス(i1,j1)(i2,j2)に加湿器がある場合、その時点でかしつされているかどうかというのは、
abs(i-i1)+abs(j-j1) <= D or 


"""

def check() :
    return


def main() :
    """ 
    - k1, k2をそれぞれ加湿器の位置
    - i1,j1 =k1を2次元形式に戻したもの
    - x,y = 調査位置
    """
    H, W, D = map(int, input().split())
    S = [input() for i in range(H)]
    result = 0
    for k1 in range(H*W-1) :
        for k2 in range(k1+1, H*W):
            i1,j1 = k1//W, k1%W
            i2,j2 = k2//W, k2%W
            #print(i2,j2)
            if S[i1][j1] == "#" or S[i2][j2] == "#" :
                continue
            tmp_result = 0
            for y in range(H) :
                for x in range(W) :
                    if S[y][x] == "#" :
                        continue
                    elif abs(y-i1)+abs(x-j1) <= D or  abs(y-i2)+abs(x-j2) <= D :
                        tmp_result += 1
            result = max(tmp_result, result)
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
