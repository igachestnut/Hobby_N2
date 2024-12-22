N = int(input())
S = input()
for i in range(1,N):
    for k in range(N-i):
        if S[k] == S[k+i]:
            print(k,"for")
            break
    else:
        print(k+1,"Lastfor")


print()
############################################################
#例外処理（S1==S2）の場合で、出力。
#それ以外はpassする。（すなわち最後までpass）
#最後もpassだった場合、elseを扱うと出力することができる
#
#すなわち
"""
if
if
if
if
if
if
else
といった感じ。

自分のは
if
else
if
else
if
else
といった感じ。

処理数てきには
「例外のみ」で適用するようにすればアルゴリズムの高速化が望める。

"""
