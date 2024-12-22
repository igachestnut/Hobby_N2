def cheaker() :
    return


def main() :
    n = int(input())
    for i in range(n) :
        binary_track = list(map(int, input().split()))
        track = ""
        for j in range(n):
            if binary_track[j] :
                track += f"{j+1} "
        print(track)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
