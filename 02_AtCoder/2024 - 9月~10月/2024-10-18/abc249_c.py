""" MEMO

2**Nだけ存在する。選び方。

Sを任意だけ抽出した場合、K個だけ文字列が出てきているその種類数を見つけだす。
全数調査

2**Nだけ、選び方があり、
26* 2**N

"""
def check() :
    print(2**15) #32768
    print(ord("a"))
    print(ord("A"))
    return


def main() :
    N, K = map(int, input().split())
    alphabets = [[0 for i in range(26)]]
    for i in range(N) :
        Si = list(input())
        new_alphabets = []
        for old_a in alphabets :
            #print(old_a)
            new_alpabet = [oa for oa in old_a] #配列の複製。今までの経路+次のsを選択したときの新規配列を作る用。
            for s in Si : 
                #print(ord(s),s)
                new_alpabet[ord(s)-ord("a")] += 1
            new_alphabets.append(new_alpabet)
        for na in new_alphabets : alphabets.append(na)
    
    result = 0
    for a in alphabets :
        result = max(result, sum([1 if ak == K else 0 for ak in a]))

    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
