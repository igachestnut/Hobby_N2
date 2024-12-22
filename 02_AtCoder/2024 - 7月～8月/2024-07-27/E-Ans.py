def cheaker() :
    return


def main() :
    N, X, Y = map(int, input().split())
    Nodes = set(tuple(0, 0, 0))
    for n in range(N) :
        a, b = map(int, input().split())
        for na, nb, ni in Nodes :
            new_node = [na+a, nb+b, ni+1]
            if new_node[0] <= X and new_node[1] <= Y :
                Nodes.add(new_node)
    #print(Nodes)
    results = [element[2] for element in Nodes]
    print(min(max(results), N))
    return

def main2() :
    N, X, Y = map(int, input().split())
    dp = [None ]


if __name__ == "__main__" :
    main()
    #cheaker()
