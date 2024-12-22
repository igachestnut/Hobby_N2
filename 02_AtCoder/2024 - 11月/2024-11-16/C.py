def check() :
    print("1"*3)
    return


def main() :
    N, K = map(int, input().split())
    S = input()

    is_search = False
    result = ""
    k_count = 0
    before_s = 0
    l, one_l, r = None,None,None #調査の開始位置から、
    for i, s in enumerate(S) :
        if is_search == False :
            if (before_s == 0 and s == "0") or (before_s == 1 and s == "1"):
                result += s
            elif before_s == 0 and s == "1" : #0の流れから初めて見つけた。
                k_count += 1
                before_s = 1
                result += s
            elif before_s == 1 and s == "0" :
                if k_count == K-1 :
                    is_search = True
                    l = i+1 #変更の開始位置
                    before_s = 0
                else :
                    before_s = 0
                    result += s
            else :
                raise ValueError("???")
        else :
            if k_count == K-1 and before_s == 0 :
                if s == "0": continue
                else :
                    one_l = i+1
                    k_count += 1
                    before_s = 1
            elif k_count == K and before_s == 1 :
                if s == "1" :
                    pass
                else :
                    before_s = 0
                    r = i+1
                    result += "1"*(r-one_l) + "0"*(one_l-l)
                    is_search = False
                    result += "0"
            else :
                print(l, one_l, l)
                print(i, s)
                print(result)
                raise ValueError("何か良からぬことが起こっています")
        #print(result)
        #print(l, one_l, l)
        #print(k_count)
    if len(result) != len(S) :
        r = i+2
        result += "1"*(r-one_l) + "0"*(one_l-l)
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
