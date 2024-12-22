""" #####################################################
発想

靴下の互い違いを最も抑えてほしい。
→一見むずそうだが、使用する靴下はA[i]のみ。

len(A) % 2 == 0 の場合、すべての靴下を使用しなければならない
→小さい順に 2つずつabsを足していけばいいだけ。

len(A) % 2 == 1の場合、使用しない靴下が1つある
- ij の取り方 N//2 +1通りある。この時の最小を見るとよさそう。
一回N//2 まで(一番最後を残した場合)を計算する。
result = 0
for i in range(0, N, 2) :
    j = i+1
    result += abs(A[i]-A[j])

tmp_result = result
for i in range(N-1, -1, -2) :
    tmp_result -= abs(A[i]-A[j]) #一つ分減らす
    tmp_result += abs(A[j]-A[k]) #奥でくくる
    result = min(result, tmp_result)



##################################################### """
def check() :
    return


def main() :
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if K %2 == 0 :
        result = 0
        for i in range(0, K, 2) :
            result += abs(A[i]-A[i+1])
        print(result)
        return
    else : #余りが奇数だが、3以上の時
        result = 0
        for i in range(0, K-1, 2) : #一度最後まで計算する
            result += abs(A[i]-A[i+1])

        tmp_result = result
        for i in range(K-3, -1, -2) :
            tmp_result -= abs(A[i]-A[i+1]) #一つ分減らす
            tmp_result += abs(A[i+1]-A[i+2]) # 奥でくくる
            result = min(result, tmp_result)
        print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
