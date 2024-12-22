N,P,Q,R,S = map(int,input().split())
A = list(map(int,input().split()))

b1 = A[P-1:Q]
b2 = A[R-1:S]
A[R-1:S] = b1 
A[P-1:Q] = b2
print(*A)
