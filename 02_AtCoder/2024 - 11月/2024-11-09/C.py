def check() :
    return


from collections import defaultdict
def main() :
    """ 発想
    N~i~1まで実行する。最も左側に位置する石を持ってくる。
    その回数をプラスする。

    N 1,2,3,4,5
    A 3,1,1,0,0
    N=5の時、
        - N=1のところから石を持ってくるの = 4回処理
        - N=3のとこらから石を持ってくる = 2回処理、余った3に1から石を持ってくる → 2回処理。したがって 2+2=4である。経路は関係ない。
    ただし、今回の制約がN<=2*10**9なので O(N)では間に合わない。
    逆にM が2*10**5なので何とかなりそう

    X,Aはソートである。
    では、山の最終位置(Nまでの要領における、余裕の位置)
    というか、山が途中で余る場合、逆に左側に石を動かす必要ができてくるだろう。
    いやいやいや、右にしか動かしてはいけない制約である。
    →経路は関係なくなる。その地点でどんなに石が余ってようとも使用しないのなら終了である。

    right_stone_position = 石が置かれているであろう最も右端の位置。入力N+1からスタート
    new_right_stone_position = max(X[i], right_stone_position-A[i], 1)
    now_put_stone_range = new_right_stone_position - right_stone_position
    all_move = (right_stone_position-X[i])*(right_stone_position-X[i]-1)//2 if right_stone_position > X[i]+1 else 0
    empty_move = (new_right_stone_position-X[i])*(new_right_stone_position-X[i]-1)//2 if new_right_stone_position > X[i]+1 else 0 #石を動かさなくても充填されている場合、動かす必要がないため動かさない
    result += 

    right_stone_position = new_right_stone_position
    """
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    A = list(map(int, input().split()))

    xa = defaultdict(int)
    for i in range(M) :
        xa[X[i]] = A[i]

    right_stone_position = N+1 #石が置かれているであろう最も右端の位置。入力N+1からスタート
    result = 0
    for i in range(M-1, -1, -1) :
        new_right_stone_position = max(X[i], right_stone_position-A[i], 1)
        #now_put_stone_range = new_right_stone_position - right_stone_position
        all_move = (right_stone_position-X[i])*(right_stone_position-X[i]-1)//2 if right_stone_position > X[i]+1 else 0
        empty_move = (new_right_stone_position-X[i])*(new_right_stone_position-X[i]-1)//2 if new_right_stone_position > X[i]+1 else 0 #石を動かさなくても充填されている場合、動かす必要がないため動かさない
        result += all_move - empty_move
        print("-----")
        print(right_stone_position, X[i], new_right_stone_position)
        print(all_move, empty_move)
        right_stone_position = new_right_stone_position        

    if right_stone_position != 1 :
        print(-1)
    else :
        print(result)
    return

from collections import defaultdict
def main2() :
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    A = list(map(int, input().split()))

    xa = defaultdict(int)
    for i in range(M) : xa[X[i]] = A[i]

    right_stone_position = N+1 #石が置かれているであろう最も右端の位置。入力N+1からスタート
    result = 0
    for x in sorted(xa.keys(), reverse=True) :
        new_right_stone_position = max(x, right_stone_position-xa[x], 1)
        all_move = (right_stone_position-x)*(right_stone_position-x-1)//2 if right_stone_position > x+1 else 0
        empty_move = (new_right_stone_position-x)*(new_right_stone_position-x-1)//2 if new_right_stone_position > x+1 else 0 #石を動かさなくても充填されている場合、動かす必要がないため動かさない
        result += all_move - empty_move
        #print("-----")
        #print(right_stone_position, x, new_right_stone_position)
        #print(all_move, empty_move)
        right_stone_position = new_right_stone_position        

    if right_stone_position != 1 :
        print(-1)
    else :
        print(result)
    return

if __name__ == "__main__" :
    main2()
    #check()
