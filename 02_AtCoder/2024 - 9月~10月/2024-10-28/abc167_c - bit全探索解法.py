""" #####################################################
発想

買う組み合わせ = 2**N通り
全数調査→ナップサック問題に似ている。

方法１
- bit全探索をして、すべての答えを導出する。
- その後、各答えは条件を超えているか調査し、超えている場合にその最小値を入力する。


MEMO - bit演算のコラム
- bitが与えられるときのj 番目が立っているかどうか確認したいとき
    方法1. (bit >> j) & 1 : bitをjだけ右シフトして、1と同じ場所が立っているか計算する
    方法2. bit & (1 << j) : 1をjだけ左シフト(でかく)して、でかくした場所とbitの位置の同じ場所が立っているか計算する。
    
    上記二つの計算結果には差異は無し。
    計算量も特に違いはないらしい?(chatGPT)調査が必要。

##################################################### """
def check() :
    return


def main() :
    N, M, X = map(int, input().split())
    book_mart = []
    for i in range(N) :
        book_mart.append(list(map(int, input().split())))

    # bit全数調査で、組み合わせの全列挙 2**N * N*M → 結果に合うか調査し、その値を入力
    result = float("inf")
    for bit in range(1 << N) :
        tmp_book_comb = [0 for m in range(M+1)]
        for j in range(N) :
            if (bit >> j) & 1 :
                for m in range(M+1) :
                    tmp_book_comb[m] += book_mart[j][m]
        #print(bit, bin(bit))
        #print(tmp_book_comb)
        # 結果の入力
        for tbc in tmp_book_comb[1:] :
            if tbc < X : break
        else :
            result = min(tmp_book_comb[0], result)

    # 結果の出力
    if result == float("inf") : print(-1)
    else : print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
