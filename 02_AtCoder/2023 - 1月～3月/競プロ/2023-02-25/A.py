def cheaker() :
    return


def main() :
    S = list(input())
    #islower,isupper,istitle
    #すべて大文字、全て小文字、最初の文字が大文字かどうか
    for i in range(len(S)) :
        if S[i].istitle() :
            print(i+1)
            return
    return


if __name__ == "__main__" :
    main()
    #cheaker()
