def cheaker() :
    return


def main() :
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result_x, result_y = 0, 0 #ＡＢそれぞれにおいて、最小食べる回数
    A.sort()
    B.sort()
    for a in A[::-1] :
        X -= a
        result_x += 1
        if X < 0 :
            break
    for b in B[::-1] :
        Y -= b
        result_y += 1
        if Y < 0:
            break
    print(min(result_x, result_y))
    return


if __name__ == "__main__" :
    main()
    #cheaker()
