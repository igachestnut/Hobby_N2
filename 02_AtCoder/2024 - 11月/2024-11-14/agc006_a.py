""" #####################################################
発想

pickupされた文字列が合同か否か判断する。
s[i:], t[:-(i+1)] 

100*100

##################################################### """
def check() :
    a = list(range(10))
    print(a[:-0])
    return


def main() :
    N = int(input())
    s = input()
    t = input()
    
    for i in range(N) :
        #print(s[i:], t[:N-i])
        if s[i:] == t[:N-i] : 
            print(2*N-(N-i)) #全部の長さ - かぶり文字の数
            return 
    else :
        print(2*N)
    return


if __name__ == "__main__" :
    main()
    #check()
