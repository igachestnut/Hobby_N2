def check() :
    return


def main() :
    K = int(input())
    S = list(input())
    T = list(input())
    if abs(len(S) -len(T)) > 1 :
        print("No")
        return

    for i in range(min(len(S),len(T))) :
        if S[i] != T[i] :
            # 挿入してOKか判定する
            if len(S) > len(T) :
                for j in range(i+1, len(S)):
                    if S[j] != T[j-1] :
                        print("No")
                        return
                else :
                    print("Yes")
                    return
                
            # 置き換えてOKか判定する
            elif len(S) == len(T) :
                for j in range(i+1, len(S)) :
                    if S[j] != T[j] :
                        print("No")
                        return
                else :
                    print("Yes")
                    return

            # 削除してOKか判定する
            else :
                for j in range(i, len(S)) :
                    if S[j] != T[j+1] :
                        print("No")
                        return
                else :
                    print("Yes")
                    return
    print("Yes")
    return


if __name__ == "__main__" :
    main()
    #check()
