""" #####################################################
発想

- Aiをうまく変えて、Biの倍数になるようにしたい!
- ボタンはi 番目を押したとき、 A1~Aiまで+=1される。

- 降順に確定するとよさそう。
- AN = 3, BN = 4 の時、
1回押す = BN - AN%BN 

んでこの時のAN は AN + result(今までボタンが押された総数である)

##################################################### """
def check() :
    return


def main() :
    N = int(input())
    AB = []
    for i in range(N) :
        AB.append(list(map(int, input().split())))
    
    result = 0
    for i in range(N-1,-1,-1) :
        push_cnt = AB[i][1] - (AB[i][0]+result)%AB[i][1]
        result += push_cnt if push_cnt != AB[i][1] else 0

    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
