def cheaker() :
    return


def main() :
    N, X, Y = map(int, input().split())
    Nodes = []
    for n in range(N) :
        a, b = map(int, input().split())
        for na, nb, ni in Nodes :
            new_node = [na+a, nb+b, ni+1]
            if new_node[0] <= X and new_node[1] <= Y :
                Nodes.append(new_node)
        if a <= X and b <= Y :
            Nodes.append([a, b, 1])
    #print(Nodes)
    if len(Nodes) == 0 :
        print(1)
        return
    results = [element[2] for element in Nodes]
    print(min(max(results)+1, N))
    return


if __name__ == "__main__" :
    main()
    #cheaker()
