#法則性より
def calculation(n) :
    """
    アルゴリズム解説
    　nを2で順々に割ると、2進数が末尾から分かる
    　頭は必ず1になる。（n>1）
    割る数を4,8にすると4進数、8進数の表現が可能
    """
    Ans = [str(0) for _ in range(10)]
    i = 0
    while n > 1 :
        n,ans = n // 2 ,n % 2
        Ans[i] = str(ans) #余り
        i += 1
    Ans[i] = str(n)
    Ans.reverse()#法則性より逆順にする
    return Ans

def main() :
    N = int(input())
    ans = calculation(N)
    print("".join(ans))
    
    

if __name__ == "__main__" :
    main()


#sequence item 0: expected str instance, int found
#TypeError　シークエンスアイテム⇒該当するアイテム
