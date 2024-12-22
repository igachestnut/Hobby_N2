N,M = map(int,input().split())

S = []
T = []
for n in range(N) :
    s = input()
    S.append(s[3:])
for m in range(M) :
    T.append(input())

#被りがあるかどうかをメモするリスト
dist = [0 for n in range(N)]

for n in range(N) :
    for m in range(M) :
        if S[n] == T[m] :
            dist[n] = 1

print(sum(dist))
