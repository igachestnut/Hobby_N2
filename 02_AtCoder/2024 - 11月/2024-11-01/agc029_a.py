""" #####################################################
発想

note
BBW BWB WBB
BBB 
BWB WBB 
BWW WBW WWB
WBB 

→ 左にW, 右にBが来るような回数の総数???


BWBBWWB WBBBWWB WBBWBWB

##################################################### """
def check() :
    return


def main() :
    S = list(input())
    white_count = 0 #whileが検知された回数
    result = 0
    for i in range(len(S)) :
        if S[i] == "W" :
            result += i-white_count
            white_count += 1
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
