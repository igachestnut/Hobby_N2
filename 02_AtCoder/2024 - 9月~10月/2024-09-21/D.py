def cheaker() :
    return

import heapq
def main() :
    N = int(input())
    H = list(map(int, input().split()))
      
    result = [0 for i in range(N-1)] + [1]
    r_query = [N-1]
    heapq.heapify(r_query)
    for i in range(N-2, -1, -1) :
        while r_query : 
            a = heapq.heappop(r_query)
            #print(a)
            if H[i] < H[a] : #もし右上がりだった場合 (現在着目している数値の方が下だよとなった場合。)
                result[i] = result[a] + 1 
                heapq.heappush(r_query, a) 
                heapq.heappush(r_query, i)
                #print(r_query)
                break
            else : #もし現在着目している数値の方が多い場合、現在の値は一つ前の+1リセットしてやり直す
                if len(r_query) == 0 : 
                    r_query = [i]
                    heapq.heapify(r_query)
                    result[i] = 1 
                    break
                #print("passします")
    result = [r for r in result[1:]] + [0]
    print(*result)
                    
    return


if __name__ == "__main__" :
    main()
    #cheaker()
