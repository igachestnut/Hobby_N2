""" 処理回数について


1. Q だけ実行
2. 時計回りして、node分だけ移動が必要 N
その他mod計算はいいかぁ...

QNですね。
"""
def check() :
    return


def main() :
    N, Q = map(int, input().split())
    hand = [0,1] #現在握っている手の位置。左がLで、右hand[1]がR
    result = 0 #最小の回数を導出する。
    for q in range(Q) :
        H, T = input().split()
        moveh = 0 if H=="L" else 1
        notmoveh = (moveh+1) %2
        i = hand[moveh]
        cw = True
        while i != int(T) -1 :
            i = (i+1) % N #時計回りで次に移動 
            if hand[notmoveh] == i :#時計回り路上に、逆手があった場合
                cw = False
        if hand[moveh] < int(T)-1 and cw :
            result += (int(T)-1) -hand[moveh]
            #print(f"時計回りに{ (int(T)-1 -hand[moveh])%N}")
        elif hand[moveh] > int(T)-1 and cw :
            result += (N-(hand[moveh]-(int(T)-1) )) %N
            #print(f"時計回りに{ (N - int(T)-1 -hand[moveh]) %N}")
        elif hand[moveh] < int(T)-1 and not cw :
            result += (N-((int(T)-1)-hand[moveh])) %N
            #print((N - (int(T)-1) -hand[moveh]) %N)
        else :
            result += (hand[moveh] - (int(T)-1)) %N
            #print( (int(T)-1 -hand[moveh]) %N)
        hand[moveh] = int(T)-1
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
