def check() :
    return


def main() :
    A = list(map(int, input().split()))
    color = [0 for i in range(5)]
    result = 0
    for i in range(4) :
        color[A[i]] += 1

    for i in range(5) :
        if color[i] >= 4 :
            result += 2
        elif color[i] >= 2 :
            result += 1
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
