""" #####################################################
発想


<>の等号が成り立つ良い非負整数配列を定義しろ。
総和は最小で。

<>>
0<2>1>0
>-< の両方が> < で囲まれた数字= 必ず0

 < > > > < < > < < < < < > > > < 
0<3>2>1>0<1<2>0<1<2<3<4<5>2>1>0<1
1*5 = 5
2*4 = 8
3*2 = 6
4+5 = 9 
ans = 28

前の数値よりどれくらい高い数値か、否かを記載する配列??
><の時必ず0 →それから値を増やしていく

x>x-1>x-2>0
の時、x-3 = 0
以前までの総和 = 初項0, 等差1, 項数4の等差数列の和?
ただし、4<5>2>1 のようなケースがある。つまりxが5で確定しているというもの
各項で定義できる最大数を記入する
for i in range(len(S)) :
if S[i] == "<" :現在位置が最小値である。

if A[i] > A[i+1]
A[i+1] == a
j = 1
while S[i-j] == ">" and i-j >= 0 :
    A[i+1] = min(A[i+1], A[i+2]+1)
a += 1

else : ">"のとき。確定できない
    a = 0 #次の初期位置ように更新

    

    
    
どうしようか...
1回目に考えた手法 → 
1. for len(S)まで実行
    1. < 初めてが生じるところ = 0(必ず低である)
    <が続けて生じた場合、1ずつ増えていく。

    もし以前までの処理が>だった場合、遡る処理を行って、最小値を確定する必要がある。






##################################################### """
def check() :
    return


def main() :
    S = list(input() + "<")
    A = [-1] * (len(S)+2)

    a = 0
    # 値を確定する処理
    for i in range(len(S)) :
        if S[i] == "<" : #現在位置が最小値である。
            # 値の確定
            A[i+1] = a
            a += 1

            # 値をさかのぼる処理
            j = 1
            while S[i-j] == ">" and i-j >= 0 : #j個遡った結果、>だった。
                A[i+1-j] = max(A[i+1-j], A[i+2-j]+1)
                j += 1
        else : #">"のとき。確定できない
            A[i+1] = a #もし初めて値が出てきた場合、現在のmaxを記入する
            a = 0 #次の初期位置ように更新
    print(sum(A[1:-1]))

    return


if __name__ == "__main__" :
    main()
    #check()
