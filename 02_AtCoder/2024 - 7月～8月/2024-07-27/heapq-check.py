import heapq

def cheaker() :
    A = [5, 2, 3]
    B = [[5, (2, 2)], [1, (2, 2)], [3, (1, 3)]]
    h = []
    for i in A :
        heapq.heappush(h, i)
    print(heapq.heappop(h))
    
    #Aなら、追加したオブジェクトの番号順(低い順)に取り出し可能。
    #Bなら1インデックス目のオブジェクト順に取り出し可能。
    
    return


def main() :
    return


if __name__ == "__main__" :
    #main()
    cheaker()
