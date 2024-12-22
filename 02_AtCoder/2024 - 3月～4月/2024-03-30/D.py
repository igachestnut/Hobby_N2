def cheaker() :
    print(len(str(2**60)))
    return


def main() :
    a, b, C = map(int, input().split())
    
    #CのBit演算
    BitC = create_BitC(C)
    popcount_C = get_popcount(BitC) #1の数取得
    
    #入力のabと比べて作成可能か吟味(偶奇を使用)
    if (a+b) % 2 != popcount_C % 2 :
        print("-1")
        return
    else :
        pass
    
    #任意の数の出力
    BitA = [0 for i in range(121)]
    BitB = [0 for i in range(121)]
    now_index = 0
    
    while a > 0 :
        if BitC[now_index % len(BitC)] :
            BitA[now_index] = 1
            a -= 1
            BitC[now_index] = 0
        now_index += 1
        
    while b > 0 :
        if BitC[now_index % len(BitC)] :
            BitB[now_index] = 1
            B -= 1
            BitC[now_index] = 0
        now_index += 1
        
    A = createNUM(BitA)
    B = createNUM(BitB)
    
    print(str(A) + " " + str(B))
    
    return

def create_BitC(X) :
    BitC = [] 
    #10進法のXを(indexの位)と見立てたリストを作成する処理
    while X > 0 :#Xが0になるまで実行する
        X, y = calucration(X)
        BitC.append(y)        
    return BitC

def calucration(x) :
    """ ある数xを2で割った値と余りを出力する """
    return x//2, x%2

def get_popcount(List) :
    """ ある渡された値のpopcountを取得する関数 """
    popcount = 0
    for i in range(len(List)) :
        if List[i] == 1 :
            popcount += 1
    return popcount


    
def createNUM(BIT) :
    Int = 0
    for i in range(len(BIT)) :
        Int += BIT[i] * 2**i
    return Int
    
    
if __name__ == "__main__" :
    #main()
    cheaker()
