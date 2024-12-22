IDcheaker = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

ID = list(input())

ID_num = 0
for i in range(len(ID)) :
    for j,a in enumerate(IDcheaker) :
        if ID[i] == a :
            ID_num += 26**(len(ID)-i-1)*(j+1)
            print(ID_num)
