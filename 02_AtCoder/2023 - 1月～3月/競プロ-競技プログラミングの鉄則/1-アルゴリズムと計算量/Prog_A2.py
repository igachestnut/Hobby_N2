#二分探索
def binary_search(a,X) :
    Min,Max = 0 , len(a)-1
    while Min <= Max :
        tmp = (Min + Max) // 2
        if a[tmp] < X :#上に存在する場合、
            Min = tmp +1#その数以下をバッサリ切る！
        elif a[tmp] == X :#値が合致した場合
            return "Yes"
        else :#下に存在する場合
            Max = tmp -1#その数以上をバッサリ切る！
            
    #while文の終了⇒合致する値が存在しなかった
    return "No"
        

def cheaker() :
    a = list(range(10,90,20))
    print(len(a)//2)
    print(a[len(a)//2])
    print(5//2)#切り捨ての流れ。

def cheaker2() :
    a = list(range(100))
    X = 75
    binary_search(a,X)

def main() :
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    print(binary_search(A,X))
        

if __name__ == "__main__" :
    main()
