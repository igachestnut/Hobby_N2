def cheaker() :
    return


def main() :
    N = int(input())
    sholder_tall  = 0 # 全員の肩の高さ
    max_head_tall = 0 #B-Aの最大高さ
    
    for n in range(N) :
        a, b = map(int, input().split())
        sholder_tall += a
        max_head_tall = max(max_head_tall, b-a)
        
    print(sholder_tall + max_head_tall)    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
