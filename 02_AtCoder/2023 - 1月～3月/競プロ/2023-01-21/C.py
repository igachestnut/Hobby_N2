from collections import deque

def Money(Str,money,A,B) :#お金の査定
    count = 0
    for j in range(len(Str)//2) :
        if Str[j] != Str[-j-1] :
            count += 1
    return count * B

def main() :
    N,A,B = map(int,input().split())
    S = deque(input())

    dist = [0 for _ in range(N)]
    money = 0
    for i in range(N) : #文字指定
        dist[i] = money + Money("".join(S),money,A,B)
        s = S.popleft()
        S.append(s)
        money += A

    print(min(dist))

if __name__ == "__main__" :
    main()
