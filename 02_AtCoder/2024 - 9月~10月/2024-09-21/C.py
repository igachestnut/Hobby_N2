def cheaker() :
    return


def main() :
    N, Q = map(int, input().split())
    S = ["#", "#"] + list(input()) + ["#", "#"]
    #print(S)
    # 全文字列を作成する
    
    sub_s = ["".join(S[i:i+3]) for i in range(N+2)]
    #print(sub_s)
    result = 0
    for s in sub_s : result += 1 if s == "ABC" else 0
    
    #queryの実行
    for q in range(Q) :
        #print(sub_s)
        x,c = input().split()
        x = int(x) -1
        r_old, r_new = 0, 0
        for i, xi in enumerate(range(x, x+3)): 
            if sub_s[xi] == "ABC" : r_old += 1 
            t_s = list(sub_s[xi]) 
            t_s[-i-1] = c
            sub_s[xi] = "".join(t_s)
            if sub_s[xi] == "ABC" : r_new += 1
        result += r_new - r_old
        print(result)
    return

if __name__ == "__main__" :
    main()
    #cheaker()
