def check() :
    return


def main() :
    safezone_map = [True for _ in range(64)]
    for i in range(8) :
        S = list(input())
        for j, s in enumerate(S) : 
            if s == "#" :
                for k in range(8) :
                    safezone_map[i*8+k] = False
                    safezone_map[k*8+j] = False
    result = sum(safezone_map)
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
