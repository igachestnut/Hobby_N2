def cheaker() :
    return


def main() :
    S = list(input())
    num_lis = list(map(int, S[3:]))
    num = num_lis[0] * 100 + num_lis[1] *10 + num_lis[2]
    #print(num)
    if 0 < num < 350 and 316 != num :
        print("Yes")
    else :
        print("No")
    return


if __name__ == "__main__" :
    main()
    #cheaker()
