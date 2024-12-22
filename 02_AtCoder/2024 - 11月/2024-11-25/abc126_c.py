""" #####################################################
発想

- 確率を求める
- 起こりうるすべての事象について記載する
    - 1.さいころを振る。K以上だった時→sunuke win!
    - 2-1.コインを振る。裏→sunuke lose!
    - 2-2-1.コインを振る。表でK以上→sunuke win!
    .....
    - 得点は常に増え続けるor0になるので、最終的にはlog(2*10**5)回だけ繰り返される

    - 起こりうる事象
        1. N
        2-1. (min(K,N)) *2

- 求めたい確率 = win / (win+lose)
- 1. N>K の時、N-K をwinに。
- 2. play = min(N,K) より、
lose += play.カウント
win += play中でKを超えたindex,K//2 以上のindex数
play = K//2までのplay


...確率というのは、
一番最初程、確率のウエイトが高い、モノですよということ。


##################################################### """
def check() :
    import bisect
    K = 100
    a = list(range(100))
    i = len(a)
    while i>1 :
        K = K//2
        i = bisect.bisect(a, K)
        print(a[:i])
    return

def main() :
    """ WAです

    この関数の出力は、起こりうるすべての事象のうち、winになったときの総数を出力している。
    これは確率ではない。 
    """
    N, K = map(int, input().split())
    K = K-1 #Kを以上ではなく、Kよりも大きいときwinという意味に変える
    win, lose, play = max(0, N-K), 0, min(N,K)
    while play>0 :
        print(f"win{win}, lose{lose}, play{play}")
        K = K//2
        lose += play
        win += max(0, play-K)
        play = min(play, K)
    print(win/(lose+win))
    return

def main2() :
    """ 
    
    - 確率を再定義、
        - さいころを振ってある出目の確率 = 1/N
        - さいころを振るだけで勝つ確率 = (N-(K-1))/N (N>=Kの時)
        - 残った出目 = 1/N のobjが obj<K 個ある
        - 残った出目が勝つ確率。
            - 1/(N*2**i) で、K>=のとき 
    """
    N, K = map(int, input().split())
    K = K-1 #Kを以上ではなく、Kよりも大きいときwinという意味に変える
    win = float(0)
    if N>K :
        win += (N-K)/N
        play = K
    else :
        play = N
    i = 1
    while play>0 :
        K = K//2
        if play>K :
            win += (play-K)/(N*2**i)
            play = K
        i += 1
    print(win)
    return


if __name__ == "__main__" :
    main2()
    #check()
