def cheaker() :
    return


import math
def main() :
    """ 
    ans = H+W C W
    
    result
    ------------
    - WA
        - 分母分子で分けて考えてみたら？
    """
    H, W = map(int, input().split())
    H, W = H-1, W-1
    ans = 1
    for w in range(1, W+1): 
        ans = (ans*(H+w)/(w)) % 1000000007
        #print(ans)
    print(int(ans))
    return

def main2() :
    H, W = map(int, input().split())
    H, W = H-1, W-1
    ans_bunnbo = 1
    ans_bunnsi = 1
    for hw in range(H+1, H+W+1): ans_bunnbo = (ans_bunnbo*hw) % 1000000007
    for w in range(1, W+1): ans_bunnsi = (ans_bunnsi*w) % 1000000007
    ans = (ans_bunnbo/ans_bunnsi) % 1000000007
    print(int(ans))
    return



if __name__ == "__main__" :
    main2()
    #cheaker()
