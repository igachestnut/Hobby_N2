
T = int(input())
for t in range(T) :
    N = int(input())
    A = list(map(int,input().split()))
    Ans = 0
    for n in range(N):
        if A[n] % 2 == 1 :
            Ans += 1

    print(Ans)
