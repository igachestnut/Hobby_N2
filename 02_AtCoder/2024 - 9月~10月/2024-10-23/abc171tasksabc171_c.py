""" #####################################################
発想

1の位の文字
mod26の答え

2の位の文字
name//26 %26 の答え??

##################################################### """
def check() :
    print(chr(2+96))
    return


def main() :
    N = int(input())
    result = []
    while N > 0 :
        result.append(chr((N-1)%26+97))
        N = (N-1)//26
    result.reverse()
    #print(result)
    print("".join(result))
    return


if __name__ == "__main__" :
    main()
    #check()
