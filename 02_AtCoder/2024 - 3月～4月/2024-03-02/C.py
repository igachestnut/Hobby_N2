def cheaker() :
    """
    for i in range(50, 100) :
        print(i+1, (i+1)**3)
    """

    return


def main() :
    N = int(input())
    a = 0
    ans = 0
    now = 0
    while now < N :
        if is_roll_number(now) :
            ans = now
        a += 1You
        #回文数の計算
        now = a**3
    print(ans)
    return

def is_roll_number(now) :
    #回文数かチェックする関数
    for i in range(len(str(now))) :
        if str(now)[i] == str(now)[-1-i] :
            pass
        else :
            return False
    return True


if __name__ == "__main__" :
    main()
    #cheaker()
