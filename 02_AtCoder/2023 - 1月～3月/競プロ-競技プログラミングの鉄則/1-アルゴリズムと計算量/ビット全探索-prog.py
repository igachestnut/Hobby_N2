

def cheaker() :
    import numpy as np
    """bit演算の確認
    andは、両方の値があるときに出力だが、
    しっかり元のメモ（a_list）の値を反映してくれるのだろうか
    and⇒両方値があるとき1、そのほか0を出力
    """
    a_list = list(range(10))
    bit = [1,1,1,0,0,0,0,0,0,1]

    #場合１npを使った演算方法
    na = np.array(a_list)
    nb = np.array(bit)
    ans1 = na @ nb #同要素数目を掛け算し、合計を出す。
    print(ans1)



    #場合3　標準な実行方法
    #ans = sum(a_list ^ bit)
    #print(ans)
    #この標準的な実行方法が分からなかった。
    #bitが1の場合だけ掛け算したいんやけどなぁ

def cheaker2() :
    """
    bit表現をつくるbinについて
    """
    print(bin(10**5))
    print(type(bin(10000)))
    print(list(bin(10)[2:]))

def bitlist(n) :#ビットのリストを出力する関数
    BitList = []
    for i in range(2**n) :
        b = list(map(int,bin(i)[2:]))
        bit = [0 for j in range(n - len(b))] + b
        BitList.append(bit)
    return BitList
    #ただ、この実装だとメモリいっぱい使っちゃうので、
    #組み込むことにしよう

def bit_cheaker(N,S,A) :#bit全探索し、該当の者があればYesをだす関数
    import numpy as np
    for i in range(2**N) :#処理O(2**N)
        b = list(map(int,bin(i)[2:]))
        bit = [0 for j in range(N - len(b))] + b #処理O(N)弱
        tmp = np.array(bit[i]) @ np.array(A)
        if tmp == S :
            return "Yes"
    return "No"

    #処理数は、O(2**N * N)となる

def main() :
    #Nカード数
    #S求めたい数字
    #Aカードの番号
    N,S = map(int,input().split())
    A = list(map(int,input().split()))
    print(bit_cheaker(N,S,A))

if __name__ == "__main__" :
    print(bitlist(5))
    #main()
