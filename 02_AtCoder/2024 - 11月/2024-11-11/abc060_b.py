""" #####################################################
発想

sum(Aの倍数集合) % B == C ?

出てくるmodは
0~B-1だけ。
modにCが出てくればYes、No

選べる数字=Aの倍数
1A, 2A = 3A
3A, 4A = 7A
なので、どんなに繰り返しても..iA 一つの文字で集合を表せる。
ここで、Bのmodが全部出てくるか調査

##################################################### """
def check() :
    return


def main() :
    A, B, C = map(int, input().split())
    b_mod = [-1 for i in range(B)]
    for i in range(1, B+1) :
        b_mod[A*i %B] = 1
    if b_mod[C] == 1 :print("YES")
    else : print("NO")
    return


if __name__ == "__main__" :
    main()
    #check()
