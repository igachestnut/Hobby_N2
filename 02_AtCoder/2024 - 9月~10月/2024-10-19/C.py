def check() :
    return


def main() :
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()

    # 使用できる箱を大きい順に使用する。
    # 2つ以上入れられないものが存在したら購入の意味なし。
    a = N-1
    b = N-2
    result = -2
    while b >= 0 :
        if B[b] < A[a] :
            result = A[a] if result == -2 else -1 #初めての場合だけ
            a -= 1
            if result == -1 : break
            continue
        a-=1
        b-=1
    if result == -2 : result=A[0]
    print(result)    
    return


if __name__ == "__main__" :
    main()
    #check()
