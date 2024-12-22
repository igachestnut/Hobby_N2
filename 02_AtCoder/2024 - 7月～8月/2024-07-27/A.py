def cheaker() :
    return


def main() :
    N = int(input())
    sweet_count = 0
    i = 0
    while sweet_count < 2 and i < N:
        i += 1
        s = input()
        if s == "sweet" :
            sweet_count += 1
        else :
            sweet_count = 0
    print("Yes" if i == N else "No")
    return


if __name__ == "__main__" :
    main()
    #cheaker()

