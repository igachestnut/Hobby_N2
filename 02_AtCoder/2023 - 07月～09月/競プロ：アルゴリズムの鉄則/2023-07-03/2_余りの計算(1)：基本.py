#問題番号A28

def cheaker() :
    return

def main2() :
    """解説の言っていることをまとめる

    足し算、引き算、掛け算による「余り」は変更されない。

    1 - 2 = -1となるが、答えは9999になる。注意。

    MEMO
      剰余性→4則演算の余り
      でかい数をそのまま計算するのではなく、一度別の形式に落とし込む

    以下、やってみる
    """
    def caluclate(board, string, value) :
        if string == "+" :
            return board + value
        elif string == "-" :
            board -= value
            if board < 0 :
                return board + 10**4
            else : return board 
        else :
            return board * value
        
    N = int(input())
    board = 0 #黒板に書かれている数
    
    for n in range(N) :
        t, a = input().split()
        board = caluclate(board, str(t), int(a)) % 10000
        print(board)
        
    return
    

def main() :
    """自分でやってみる

    計算量について考える。
    N回繰り返す
    　四則演算1回。
    　割り算一回。

    Nは10**6まで。
    一見　O(N*2)だから大丈夫そう。
    でもうまくいかなかった。TLE

    ※C++だと最大量のエラーが生じるらしい。
    　→オーバーフローってやつ。10**20の情報量になる。

    ※pythonだと、計算における値の上限は無いけど、その分計算に時間がかかる。
    　→TLEとなる

    
    
    """
    def caluclate(board, string, value) :
        if string == "+" :
            return board + value
        elif string == "-" :
            return board - value
        else :
            return board * value
        
    N = int(input())
    board = 0 #黒板に書かれている数
    
    for n in range(N) :
        t, a = input().split()
        board = caluclate(board, str(t), int(a))
        print(board % 10000)
        
    return


if __name__ == "__main__" :
    main()
    #cheaker()
