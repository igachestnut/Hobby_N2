def cheaker() :
    return


def main() :
    N, T = map(int, input().split())
    player_score = [0 for i in range(N)]
    for _ in range(T) :
        a, b = map(int, input().split())
        player_score[a-1] += b
        print(len(set(player_score)))
    return


if __name__ == "__main__" :
    main()
    #cheaker()
