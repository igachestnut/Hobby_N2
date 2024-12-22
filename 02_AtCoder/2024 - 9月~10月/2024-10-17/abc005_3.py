""" #####################################################
発想


##################################################### """
def checker() :
    return


def main() :
    """ 今使える最も古いたこ焼きを見つけ出す。

    Aの任意要素をiとする。Bの任意要素をjとする。
    1. j を1~Mまで実行する。
        1. Aを進めていき、T以内の範囲内で渡せるたこ焼きを見つける。
        - この際、A[i]>B[j]となる場合、渡せるたこ焼きがない→noとなる。
    """
    T = int(input())
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    i = 0
    for j in range(M) :
        while i < N and A[i] < B[j] - T : i += 1 #使用できるたこ焼きまで移動する。古すぎる場合だけ次のたこ焼きに着目する。
        if i >= N or A[i] > B[j]: #もう在庫なし or #現在着目しているたこ焼きがまだ出来上がっていない場合
            print("no")
            return
        else :
            i += 1 #たこ焼きをお客さんに渡す。(roop終了)
    print("yes")
    return


if __name__ == "__main__" :
    main()
    #checker()
