N = int(input())
S = list(input())

i = 0
Ans = []
while i < N-1 :
    Ans.append(S[i])
    if S[i] == 'n' and S[i+1] == 'a' :
        Ans.append('y')
    i += 1
Ans.append(S[i])

print("".join(Ans))

"""一例
n = int(input())
s = list(input())
ans = []
for i in range(n):
    if i >= 1 and ans[-1] == "n" and s[i] == "a":
        ans.append("y")
    ans.append(s[i])
print("".join(ans))


ans.appendを増やさないために、敢えてifを増やしたてきな。
"""
