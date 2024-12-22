def cheaker() :
    return


def main() :
    S = input()
    T = list(input())
    
    s_index = 0
    correct_numbers = []
    for i, t in enumerate(T) :
        if t == S[s_index] :
            s_index += 1
            correct_numbers.append(i+1)
        
    print(*correct_numbers)
    return


if __name__ == "__main__" :
    main()
    #cheaker()
