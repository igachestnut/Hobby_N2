def cheaker() :
    return


def main() :
    S = list(input().split())
    result = [0, 0, 0]
    result[0] += 1 if S[0] == ">" else 0
    result[0] += 1 if S[1] == ">" else 0
    result[1] += 1 if S[0] == "<" else 0
    result[1] += 1 if S[2] == ">" else 0
    result[2] += 1 if S[1] == "<" else 0
    result[2] += 1 if S[2] == "<" else 0
    #print(result)
    for ans, r in zip(["A", "B", "C"], result) :
        if r == 1 :
            print(ans)
            return
    return


if __name__ == "__main__" :
    main()
    #cheaker()
