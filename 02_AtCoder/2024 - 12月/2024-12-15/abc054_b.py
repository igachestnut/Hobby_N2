""" #####################################################
発想

- N*Nの画像A, 
- M*Mの画像Bがある
- それぞれは2値画像。白黒である
- BがAに部分一致するか見て

- 部分一致するか見るために必要な計算量を考える。
1. 左上を始点として、N*N 回見る。
2. 一つの点を始点としたとき、M*M 回一致度を見る。
...O(N**2 * M**2) 50*50 = 2500 より、 3*10**3 **2 = 9*10**6 で全数でも高速。
- しいて言うなら、2.において、Mの配列分だけ調査しないといけないので、
1.の工程で見るべき量が (N-M)*(N-M)である。
N**2 - 2NM + M**2 ? 

##################################################### """
def check() :
    N = 3
    for i in range(N) :
        print(hash("Hello World!"))

    return


def main() :
    N,M = map(int, input().split())
    A,B = [], []
    for i in range(N) : A.append(list(input()))
    for i in range(M) : B.append(list(input()))

    def is_match(i,j) -> bool:
        # 左上位置 i,j において、Bと部分一致するかな?
        for y in range(M) :
            for x in range(M) :    
                if A[i+y][j+x] != B[y][x]: 
                    return False
        return True
    
    for i in range(N-M+1) :
        for j in range(N-M+1) :
            if is_match(i,j) :
                print("Yes")
                return
    print("No")
    return




if __name__ == "__main__" :
    main()
    #check()
