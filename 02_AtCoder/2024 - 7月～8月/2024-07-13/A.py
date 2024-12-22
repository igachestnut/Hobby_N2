def cheaker() :
    return


def main() :
    R, G, B = map(int, input().split())
    d = {
        "Red" : R,
        "Green" : G,
        "Blue" : B
    }
    C = input()
    d[C] = 101
    print(min(d.values()))
    return


if __name__ == "__main__" :
    main()
    #cheaker()
