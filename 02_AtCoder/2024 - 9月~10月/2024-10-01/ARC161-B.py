def cheaker() :
    count, N = 0, 10**18
    while N > 0 :
        N = N >> 1
        count += 1
    print(count)

    #10**18 は 2**60である。 これらの2進数の通りは \sum{i=3}^{60} iC3 である。
    #60C3 < 3.6 * 10**6であるため、5*10**18 以下(2*60以下)で考えられるすべての二進数を列挙してbisectでよさそう。
    return

def check2() :
    print(2**60)
    return

import bisect
def main() :
    three_bits_numbers = []
    for i in range(60, 1, -1) :
        for j in range(i-1, 0, -1) :
            for k in range(j-1, -1, -1) :
                three_bits_numbers.append(2**i + 2**j + 2**k)
    three_bits_numbers.sort()

    T = int(input())
    for i in range(T) :
        N = int(input())
        ans_i = bisect.bisect(three_bits_numbers, N)
        if ans_i == 0 : print(-1)
        else : print(three_bits_numbers[ans_i-1])

    return


if __name__ == "__main__" :
    main()
    #check2()

