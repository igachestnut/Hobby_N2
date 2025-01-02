""" #####################################################
発想


ai=1 の時, 長方形のx<xiを満たす領域
ai=2 の時, 長方形のx>xiを満たす領域

- 発想
長方形を小さくしていく。

(0,H), (W,H)
(0,0), (W,0)
の長方形があるとき
ai = 1 or 2なら、x(index0)の数値をずらす。
上=H
下=0
右=W
左=0

...制約がW,H <= 100で N<= 100なので、黒く塗りつぶすシミュもできたね。
1回のクエリで、100x100を塗りつぶすことが最大っぽそうなので
O(N*(HW))ですね。

といた方式は O(N)だね

##################################################### """
def check() :
    return


def main() :
    W,H,N = map(int, input().split())
    buttom,top,left,right = 0,H,0,W
    for i in range(N) :
        x,y,a = map(int, input().split())
        if a==1 :
            left = max(x, left)
        elif a == 2 :
            right = min(x, right)
        elif a == 3 :
            buttom = max(y, buttom)
        elif a == 4 :
            top = min(y,top)
    
    if left >= right or buttom >= top :
        print(0)
    else :
        print((right-left)*(top-buttom))
    return


if __name__ == "__main__" :
    main()
    #check()
