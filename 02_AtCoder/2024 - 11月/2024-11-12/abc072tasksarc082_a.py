""" #####################################################
発想


X = ai のiの個数の最大化。
ai は ai-1, ai, ai+1
の範囲で分岐する。
移動可能なaiを全取得して、その最大値を記入するようにする
##################################################### """
def check() :
    return


from collections import defaultdict
def main() :
    N = int(input())
    A = list(map(int, input().split()))
    a_range = defaultdict(int)
    for i in range(N) :
        for j in range(-1, 2) :
            a_range[A[i]+j] += 1

    result = 0
    for key in sorted(a_range.keys()) :
        if key < 0 or key > 10**5 : continue
        else :
            result = max(result, a_range[key])
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
