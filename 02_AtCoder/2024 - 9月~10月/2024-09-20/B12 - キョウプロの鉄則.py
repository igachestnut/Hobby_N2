""" 
発想

x^3, x 
必ず決まっている。答えで二分探索する方法

fx = x^3 + x であることより、
答えの範囲は、N//3 +2くらいまでで良い。
その中を二分探索で求める。

bisectが使用できないタイプのアイデア

- 所要時間
結局2日かかっちゃった。


"""

def cheaker() :
    return


def main() :
    """ N < 10**6 より, 探索範囲は1~N//3+2位まででよいという、O(N)実装
    
    ただ、if文で3.9999996 == 4 二ならない場合があり、間違いが生じてしまう。
    """
    N = int(input())
    result = 0
    for x in range(1, (N)//3 +2) : 
        if int((N-x)**(1/3)) == x : 
            print(x)
            return
        print(f"No N{N}, x{x}, calu{(N-x)**(1/3)}")        
    return

def main2() :
    """ キョウプロ本より、答えでの二分探索の実施をするもの。
    
    WA : 
        理由 : 答えが0.001以下で違くなる可能性がある為。
        
    """
    
    N = int(input())
    
    down, up = 1, int(pow(N, 1/3)) #(N=2の時用)
    #print(up)
    while abs(down - up) > 1 : #差が1になるまで実行する。(最も結果に近いであろう上下に近づいて終了する)
        tmp = (down + up) //2
        tmp_fx = tmp**3 + tmp
        #print(f"down{down}, tmp{tmp}, up{up}")
        if N == tmp_fx : #答えと合致した場合
            print(tmp)
            return
        elif N < tmp_fx : #答えの方が大きかった場合、up以上に答えは存在しない。
            up = tmp - 1
        else : #答えの方が小さい場合、down以下に答えは存在しない。
            down = tmp + 1

    if down**3 + down == N: print(down)
    elif up**3 + up == N: print(up)
    else: print(-1)
    return 

def main3() :
    """ キョウプロ本より、答えでの二分探索の実施をするもの。"""
    RESOLUTION = 0.0001 #分解能
    N = int(input())
    
    down, up = 1.0, pow(N, 1/3) #(N=2の時用)
    #print(up)
    while abs(down - up) > RESOLUTION : #差が1になるまで実行する。(最も結果に近いであろう上下に近づいて終了する)
        tmp = (down + up) /2
        tmp_fx = tmp**3 + tmp
        #print(tmp)
        #print(f"down{down}, tmp{tmp}, up{up}")
        if N == tmp_fx : #答えと合致した場合
            print(tmp)
            return
        elif N < tmp_fx : #答えの方が大きかった場合、up以上に答えは存在しない。
            up = tmp - RESOLUTION
        else : #答えの方が小さい場合、down以下に答えは存在しない。
            down = tmp + RESOLUTION

    print((down + up) /2)
    return 

if __name__ == "__main__" :
    main3()
    #cheaker()
