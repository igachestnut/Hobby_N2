def checker() :
    return

def main2() :
    S = input()
    
    result = 0
    for i in range(26) : #アルファベットの番号順
        str_index = [] #出てきた番号を格納するリスト。
        for j in range(len(S)-1, -1, -1) :
            if i == ord(S[j]) - ord("A") :
                str_index.append(j)
        str_index.sort()
        if len(str_index) <= 1 : continue
        for s in range(len(str_index)-1) :
            for t in range(s+1, len(str_index)) :
                result += str_index[t]-str_index[s]-1
    print(result)
    return



if __name__ == "__main__" :
    main2()
    #checker()
