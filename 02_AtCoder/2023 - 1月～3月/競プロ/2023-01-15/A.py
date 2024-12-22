"""
G = [ -1 for i in range(15)]

i = 0
while i < 16 :
    i+= 1
    
    for j in range(i+1,i+3):

こんな問題の解き方になるとは
まじで不本意

ぜったいにあとでやり直す

BFSチックに解く！
"""

G = [[2,3],[4,5],[6,7],[8,9],[10,11],[12,13],[14,15]]
for i in range(8) :
    G.append([])

a,b = map(int,input().split())

if b in G[a-1] :
    print("Yes")
else :
    print("No")

