def cheaker() :
    return


def main() :
    T = int(input())

    for i in range(T) :
        N,D,K = map(int,input().split())
        dist = [False for _ in range(N)]
        x = 0


        while K > 0 :
            dist[x] = True#丸を付ける
            K -= 1
            x = (x+D)%N
            #丸をしていないところまで続ける
            if dist[x] == True :
                while dist[x] == True :
                    K,x = K-1,(x+1)%N
        print(x)
            
    return


if __name__ == "__main__" :
    main()
    #cheaker()
