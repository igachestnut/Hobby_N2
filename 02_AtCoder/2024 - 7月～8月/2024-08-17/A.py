def cheaker() :
    return


def main() :
    A, B, C = map(int, input().split())
    if B < C : #就寝時間が日をまたいでいない場合
        if B < A < C :
            print("No")
        else :
            print("Yes")
    else : #就寝時間が日をまたいでいる場合
        if C < A < B :
            print("Yes")
        else :
            print("No")
    return


if __name__ == "__main__" :
    main()
    #cheaker()
