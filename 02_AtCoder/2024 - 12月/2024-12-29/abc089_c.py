""" #####################################################
発想

- MARCH
- MARCH のいずれかで始まる人で列挙。
- それぞれの乗算。
...ただし、この中から3人選べばよい。

11100
11010
11001
10110
10101
10011
01110
01101
01011
00111
m*a *(r+c+h) 
m*r*(c+h)
m*c*h
a*r*(c+h)
a*c*h
r*c*h

##################################################### """
def check() :
    return


def main() :
    N = int(input())
    MARCH_cnt = [0] *5
    for i in range(N) :
        s = input()
        if s[0] == "M": MARCH_cnt[0] += 1 
        elif s[0] == "A": MARCH_cnt[1] += 1 
        elif s[0] == "R": MARCH_cnt[2] += 1 
        elif s[0] == "C": MARCH_cnt[3] += 1 
        elif s[0] == "H": MARCH_cnt[4] += 1 
    
    result = 0
    for a in range(3) :
        for b in range(a+1, 4) :
            if MARCH_cnt[a] == 0 or MARCH_cnt[b] == 0 :
                continue
            result += MARCH_cnt[a]*MARCH_cnt[b]*sum(MARCH_cnt[b+1:])
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
