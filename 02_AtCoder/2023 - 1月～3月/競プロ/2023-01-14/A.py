
N = int(input())
count = 0

for i in range(10**9,10**10) :
    tmp = list(str(i))
    print(tmp)
    if tmp[0] == tmp[1] and tmp[5] == tmp[6] and tmp[7] == tmp[9] :
        count += 1
        if count == N :
            print(i)
            break

