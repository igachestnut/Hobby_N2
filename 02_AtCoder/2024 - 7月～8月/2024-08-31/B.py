def cheaker() :
    return


def main() :
    N = int(input())
    now_hand_position = [None, None]
    result = 0
    for i in range(N) :
        a, s = input().split()
        if s == "L" :
            if now_hand_position[0] :#初期位置が決まっている場合
                result += abs(now_hand_position[0] - int(a))
            now_hand_position[0] = int(a)
        else :
            if now_hand_position[1] :#初期位置が決まっている場合
                result += abs(now_hand_position[1] - int(a))
            now_hand_position[1] = int(a)
    print(result)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
