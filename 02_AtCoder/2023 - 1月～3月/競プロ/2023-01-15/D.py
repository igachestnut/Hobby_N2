def Grah() :
    #dist⇒全ての頂点
    dist = [0 for i in range(N)]
    que = []
    for i in range(len(dist)) :
        if dist[i] :
            continue
        else :
            dist[i] = True

            que = T[i]
            for j in range(N) :
                if que == S[j] :
                    dist[j] == True
                    que = T[i]
                else :
                    break
                
            
def grah(dist,que) :
    for j in range(N) :
        if que == S[j] :
            dist[j] == True
            que= T[j]
            grah(dist,que)
        else :
            return dist




N = int(input())
S,T = [],[]
for n in range(N):
    a,b = map(str,input().split())
    S.append(a)
    T.append(b)

Set = set(S + T)
print(Set)

