""" #####################################################
発想

rを固定して考える。
(l, r) が要件を満たすとき、この時のlをdrとする。
(l+1, r)も要件を満たすよねという考え方。

では、rを1~M まで計算したらよい。
この際、各rに対応する、最大左位置drを導出する
rが更新されたとき、Riを発見したら、max(dr, Li+1)である。

Rの順序でheaqpを使うとdrを求められそう。
だが、heaqpの計算量はlogNなので、drの配列を作成するためにはNlogNかかりそう。
解説の全体計算量はO(N+M)で、おそらくdrの導出にNだけしかかかっていない。
どうやって計算しているのだろうか?

いや、もしかしたら, 任意Nが与えられるとき、
Ri時点でのdrは、Li+1であることが確定している。
そして、rを計算する途中で、drを更新する処理をすればO(N+M)で行けそう。

##################################################### """
def check() :
    return


def main() :
    N, M = map(int, input().split())
    dr = [1 for i in range(M+1)]
    for _ in range(N) :
        L, R = map(int, input().split())
        dr[R] = max(L+1, dr[R]) #rをRと固定したときの、dr(条件OKな範囲)を入力から仮定義
    result = 0
    for r in range(1, M+1) :
        dr[r] = max(dr[r-1], dr[r])
        result += r-dr[r]+1 
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
