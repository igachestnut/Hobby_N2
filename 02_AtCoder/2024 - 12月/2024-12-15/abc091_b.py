""" #####################################################
発想

- 青いカードN枚, 赤いカードM枚
si, ti 

文字列を一つ宣言する。
青に合ったら+=1円。赤ならマイナス。
完全一致のみお金のやり取りが発生する。
最大何円もらえる??
##################################################### """
def check() :
    return


from collections import defaultdict
def main() :
    cards = defaultdict(int) #カードの種類と、合計スコアを格納する辞書
    N = int(input())
    for i in range(N) :
        s = input()
        cards[s] += 1
    M = int(input())
    for j in range(M) :
        t = input()
        cards[t] -= 1
    
    result = 0
    for value in cards.values() :
        result = max(result, value)
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
