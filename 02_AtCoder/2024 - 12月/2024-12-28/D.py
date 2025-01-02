


from collections import defaultdict
import heapq
def main() :
    N,M = map(int, input().split())
    row_dic, col_dic = defaultdict(list), defaultdict(list)
    for m in range(M) :
        x,y,c = input().split()
        row_dic[y].append([int(x),c])
        col_dic[x].append([int(y),c])
    
    rw_min = float("inf")
    for rkey in sorted(row_dic.keys()) :
        values = row_dic[rkey]
        heapq.heapify(values)
        while values :
            [_,nex_c] = heapq.heappop(values)
            if bef_c=="W" and nex_c=="B" :
                print("No")
                return
            bef_c = nex_c
    for values in col_dic.values() :
        heapq.heapify(values)
        [_, bef_c] = heapq.heappop(values)
        while values :
            [_,nex_c] = heapq.heappop(values)
            if bef_c=="W" and nex_c=="B" :
                print("No")
                return
            bef_c = nex_c
    print("Yes")
    return  


def check() :
    row_dic, col_dic = defaultdict(list), defaultdict(list)
    row_dic[2].append(30)
    print(row_dic[2])
    return

def main2() :
    N,M = map(int, input().split())
    row_dic, col_dic = defaultdict(list), defaultdict(list)
    for m in range(M) :
        x,y,c = input().split()
        row_dic[int(y)].append([int(x),c])
        col_dic[int(x)].append([int(y),c])
    
    rw_min = float("inf")
    #print(row_dic.keys())
    #input(sorted(row_dic.keys()))
    for rkey in sorted(row_dic.keys()) :
        #print("-----------")
        #print(rkey)
        values = row_dic[rkey]
        heapq.heapify(values)
        while values :
            [x,c] = heapq.heappop(values)
            if c == "W" :
                rw_min = min(rw_min,x)
                #print(rkey)
                #print(rw_min)
            else :
                if rw_min <= x :
                    print("No")
                    return

    cw_min = float("inf")
    for ckey in sorted(col_dic.keys()) :
        values = col_dic[ckey]
        heapq.heapify(values)
        while values :
            [y,c] = heapq.heappop(values)
            if c == "W" :
                cw_min = min(cw_min,y)
            else :
                if cw_min <= y :
                    print("No")
                    return
    print("Yes")
    return  

if __name__ == "__main__" :
    main2()
    #check()
