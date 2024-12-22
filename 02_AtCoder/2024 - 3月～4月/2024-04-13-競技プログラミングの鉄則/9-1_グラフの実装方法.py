""" ###################################
初見で解いた。AC

どうやら、この実装方法は
隣接リスト表現に分類されるらしい。

他にも「隣接行列表現」というものがある。
    0~N-1 までの正方2次元行列。
    該当場所をTrueにする。
    例) a=1, b=2 なら
    Map[0][1], Map[1][0] = True, True

    まぁ、作成されるMapが極大になりやすい。
    →場合によっての実装だね。
    
    

################################### """



def cheaker() :
    return


def main() :
    N, M = map(int, input().split())
    
    Map = [set() for n in range(N)]
    for m in range(M) :
        a, b = map(int, input().split())
        Map[a-1].add(b)
        Map[b-1].add(a)
    
    for n in range(N) :
      if not Map[n] :
        print(f"{n+1}: " +"{}")
      else :
        print(f"{n+1}: " +str(Map[n]))
    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
