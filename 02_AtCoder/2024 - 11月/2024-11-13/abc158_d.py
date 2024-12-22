""" #####################################################
発想

反転か、正転状態に、頭orけつに配列を追加する。
挙動としてわかりやすいのは query=1の時、reverse処理をすることだが、
O(N)時間かかってしまうため、log(N) or (1)を目指す必要があるということ。

queryごとに考える
順転状態で2が与えられたとき
F=1先頭に追加処理 = 先頭
F=2末尾に追加処理 = 末尾

反転状態で2が与えられたとき
F=1先頭に追加処理 = 末尾
F=2末尾に追加処理 = 先頭

先頭= insert(index, obj)
末尾= append(obj)
もしくは、ケツ側と頭側それぞれにsを作って
s_head = ""
s_tail = s
S = [s_head, s_tail]
mode = 0 #0が正転状態、1が反転状態


#################################################### """
def check() :
    return


def main() :
    S = ["", input()] #head, tail. [0]には逆順の先頭配列があり、[1]には末尾の配列がある
    mode = 0
    Q = int(input())
    for q in range(Q) :
        query = list(input().split())
        if query[0] == "1" :
            mode = (mode+1)%2
        else :
            if query[1] == "1" :
                S[mode] += query[2]
            else :
                S[(mode+1)%2] += query[2]
    if mode == 0 :
        result = S[0][::-1] + S[1]
    else :
        result = S[1][::-1] + S[0]
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
