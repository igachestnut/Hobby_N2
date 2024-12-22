
N = int(input())
S = input()

for i in range(1,N) :
    count = 0
    for k in range(N-i) :
        if S[k] != S[k+i] :
            count += 1
        else :
            break
    print(count)

"""
N = int(input())
S = input()
for i in range(1,N):
    for k in range(N-i):
        if S[k] == S[k+i]:
            print(k)
            break
    else:
        print(k+1)


TLEのない他人のプログラム
131 ms

自分
2066 ms

違い
　⇒countがあるかどうか



処理数の低減のため、+=などの処理は最小限にしないといけない。

それが必要なのは、結果がfor文で回せないような時。？
メモする的な。


新しいテクニック
for文の最後に
else:
を入れると、
最後ifのelseを出力することができる。
全てifで通った場合？的な？
"""
