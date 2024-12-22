N = int(input())

count = 0
for n in range(N) :
    if input() == "For" :
        count+= 1

print(N//2)
if count > N//2 :
    print("Yes")
else :
    print("No")
