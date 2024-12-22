def cheaker() :
    return


def main() :
    D = int(input())
    N = int(input())
    
    attendee = [0 for i in range(D+1)] #出席者のデータ構造。前日からの変化を記す形で記載している。初期値は0人出席. 最終日+1日で0人になる
    for i in range(N) :
        l, r = map(int, input().split())
        attendee[l-1] += 1
        attendee[r] -= 1

    result = 0
    for i in range(D) : 
        result += attendee[i]
        print(result)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
