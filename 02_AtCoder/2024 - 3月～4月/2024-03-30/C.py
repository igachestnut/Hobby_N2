"""
なぜか一つだけWAになってしまって正解できなかった。

どんなケースが網羅できていないのかよくわからない。

28txtに敗北


"""
import random


def cheaker() :
    print(0%1000)
    
    return


def main() :
    N, A, B = map(int, input().split())
    D = list(map(int, input().split()))
    
    #何曜日目かの算出(Dataから日数情報を除外)
    for i in range(N) :
        D[i] = D[i] % (A+B)
    
    D.sort()
    #最小値の算出 （一番曜日が速い予定を、休日の一番最初にもってくる）
    Min = min(D)
    R = random.randint(1,1000)
    
    #休日の頭をそろえる。(0が休日の初めの日)
    for i in range(N) :
        D[i] = D[i] - Min - R
    
    #print(D)
    #全て休日以内の予定かの調査
    if max(D) < (A-R) :
        print("Yes")
    else :
        print("No")
        
    return


if __name__ == "__main__" :
    main()
    #cheaker()
