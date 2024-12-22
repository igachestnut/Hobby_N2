def cheaker() :
    return


def main() :
    """ O(N * (1+3))  1+3 は初動の計算+1回ずつ引く計算量 """
    N = int(input())
    H = list(map(int, input().split()))
    T = 0
    T_qritical = [1,1,3]
    
    result = 0
    for h in H :
        result += h // 5 * 3
        h = h % 5
        while h > 0 :
            result += 1
            h = h - T_qritical[0]
            tq = T_qritical.pop(0)
            T_qritical.append(tq)
    print(result)
    return

if __name__ == "__main__" :
    main()
    #cheaker()
