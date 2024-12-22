def check() :
    return


def main() :
    """ ビルにデコレーションする

    - N<3*10**3 なので、1つずつ見ていく
    - H<3*10**3 である。

    - 全数調査O(N**3)
    - 始点i 1~i~N
    - 飛び飛びの値j 1~N
    - j1,j2 を見比べて同じならr+=1 違うならr=0で開始(これをNの配列外まで繰り返す)
    
    ..全数調査2
    - 飛び飛びの値i 1~i~Nと定義
    - i=0を始点として、2i ごとに飛び飛びの値を見て最大値を調査..1
    - これをi~2i-1 まで繰り返す。...(2)
        - (1)+(2)の計算量が合計でO(N)になりそう

    ...result は継続数なので、ビルの総数にするため+1して出力する
    """
    N = int(input())
    H = [-1] + list(map(int, input().split()))

    result = 0
    for i in range(1, N+1) : #飛び飛びの数値
        for j in range(i) : #始点のずれ 0~i-1
            k = 1+j
            tmp_r = 0
            while k+i < N+1 :
                #print(k)
                if H[k] == H[k+i] :
                    tmp_r += 1
                else :
                    result = max(result, tmp_r)
                    tmp_r = 0
                k = k+i
            result = max(result, tmp_r)
    print(result+1)
    return


if __name__ == "__main__" :
    main()
    #check()
