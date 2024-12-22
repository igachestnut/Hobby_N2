""" 
ある人の正解のケース？


"""

N,A,B = map(int,input().split())
D_LIST = list(map(int,input().split()))
ANSWER = "No"

for i in range(N):
    D_LIST[i] %= A+B

D_LIST = list(set(D_LIST))
D_LIST.sort()

for i in range(len(D_LIST)):
  if i > 0:
    if D_LIST[i] - D_LIST[i-1] > B:
      ANSWER = "Yes"
      break
  else:
    if D_LIST[i] + (A+B) - D_LIST[i-1] > B:
      ANSWER = "Yes"
      break

print(ANSWER)

