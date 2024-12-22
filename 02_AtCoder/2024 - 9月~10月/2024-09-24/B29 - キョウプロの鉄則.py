def cheaker() :
    for i in range(2, 10) :
        result = pow(13, i)
        print(result)
    
    return

def check_bit_shift() :
    """ ビットシフト演算の挙動を確認する """
    N = 1000

    result = N
    for i in range(10) :
        result = result >> 1
        print(result)
    return

def main() :
    """ 繰り返し二乗法 """
    a, b = map(int, input().split())
    
    result = 1
    while b > 0 :
        if b % 2 == 1 : result = (result * a) % 1000000007
        b = b >> 1 #ビットシフト。//2と同じ処理効果だが、 
        a = (a*a) % 1000000007
    print(result)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
    #check_bit_shift()