def cheaker() :
    print(2**92)
    return


def main() :
    H = int(input())
    
    ph = 0
    for i in range(100) :
        ph += 2**i
        if ph > H :
            print(i+1)
            return
    return


if __name__ == "__main__" :
    main()
    #cheaker()
