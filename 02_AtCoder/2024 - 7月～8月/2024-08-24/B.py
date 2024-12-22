""" 第2要素が0になるまで引く。→ソート→引く

引く作業前に、第二要素=0なら終了

"""

def cheaker() :
    return


def main() :
    N = int(input())
    A = list(map(int, input().split()))
    result = 0
    A.sort()
    while A[-2] != 0 :
        result += A[-2]
        A[-1] = A[-1] - A[-2]
        A[-2] = 0
        A.sort()

    print(result)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
