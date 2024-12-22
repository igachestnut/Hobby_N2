def check() :
    return


def main() :
    N = int(input())
    result = 0
    tmp_t = 0
    for i in range(N) :
        t, v = map(int, input().split())
        result = max(0, result-(t-tmp_t)) + v
        tmp_t = t
        #print(tmp_t, result)
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
