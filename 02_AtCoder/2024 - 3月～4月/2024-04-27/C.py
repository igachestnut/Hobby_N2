def cheaker() :
    return


def main() :
    N = int(input())
    A = list(map(int, input().split()))
    
    box = []
    #処理の開始 N回の作業
    for n in range(N) :
        box.append(A[n]) # ボールを追加する
        
        # 1.の判定
        while len(box) != 1 :
            # 2.の判定
            if box[-1] != box[-2] :
                break
            # 3.の判定
            else :
                #print(box)
                p = box.pop()
                box[-1] += 1
                #print(box)
        
    print(len(box))
    return


if __name__ == "__main__" :
    main()
    #cheaker()
