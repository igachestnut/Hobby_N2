""" #####################################################
発想

- 塗分けて。
- N個に分割してね。

- 塗りかた
 12345
 a9876
 bcde
 ..のようにしようかな。これなら

##################################################### """
def check() :
    return


def main() :
    H,W = map(int, input().split())
    N = int(input())
    A = list(map(int, input().split()))
    result = []
    for i,a in enumerate(A) :
        for j in range(a) :
            result.append(i+1)
    #print(result)
    #print(len(result))
    #input()
    
    for i in range(H) :
        tmp_r = result[i*W:i*W+W]
        if i %2 == 1:
            tmp_r.reverse()
        print(*tmp_r)
    return


if __name__ == "__main__" :
    main()
    #check()
