def cheaker() :
    a = dict()
    a[1] += 1
    return


def main() :
    Q = int(input())
    box = dict()
    for i in range(Q) :
        que = list(map(int, input().split()))
        
        #queの処理
        if que[0] == 1 :
            try :
                box[que[1]] += 1
            except KeyError:
                box[que[1]] = 1
        elif que[0] == 2 :
            box[que[1]] -= 1
            if box[que[1]] == 0 :
                del box[que[1]]
        else :
            print(len(box))
    return


if __name__ == "__main__" :
    main()
    #cheaker()
