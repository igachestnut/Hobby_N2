""" #####################################################
発想

作成できる文字列の種類について数え上げ。
N= len(S)とする
N=3の時
1,2
1,3
2,3 
N(N-1)//2

N=4の時
1,2
1,3
1,4
2,3,
2,4
3,4
N(N-1)//2
入れ替えて可能な文字列の総数 = N(N-1)//2だけである。
最大数はこれ。

ちょうど1回だけ変えるということ、
S[i] != S[j] であればどんな条件でもよさそう。
逆にS[i] == S[j]の回数だけ数え上げれば答え出そう。

A~Zまで実行する、
1a, 2a
1a, 3a
2a, 3a
これも出てきている文字列の N(N-1)//2でありそう。
がなくなるんじゃなくて、1になりそう
-3 +1

1a, 2a
1a, 3a
1a, 4a
2a, 3a
2a, 4a
3a, 4a 
これらを入れ替えても同じ文字列が生成される。

aabb
12 aabb
13 baab
14 bbaa
23 abab
24 abba
34 aabb
あれ?答えは5なんだが...
出力は5

4*3//2 = 6
同じ文字列が生じた場合は、全部で,1を追加すればよくね??

##################################################### """
def check() :
    return


def main() :
    S = input()
    alpabet = [0 for i in range(26)] #各アルファベットが出てくる回数だけ記載するリスト
    for s in S :
        alpabet[ord(s)-ord("a")] +=1
    
    N = len(S)
    result = (N*(N-1))//2 
    is_duplication = 0
    for i in range(26) :
        if alpabet[i] < 2 : continue
        result -= (alpabet[i]*(alpabet[i]-1))//2 -1#文字列は入れ替えなくても必ず1つは存在する→+1をする
    print(result)
    return

def main2() :
    S = list(input())
    alpabet = [0 for i in range(26)] #各アルファベットが出てくる回数だけ記載するリスト
    for s in S :
        #print(s)
        alpabet[ord(s)-ord("a")] +=1
    
    N = len(S)
    result = (N*(N-1))//2 
    is_duplication = 0
    for i in range(26) :
        if alpabet[i] < 2 : continue
        else :
            result -= (alpabet[i]*(alpabet[i]-1))//2 #重複を利用した場合のすべての入れ替え条件を減算する
            is_duplication = 1
    print(result+is_duplication)
    return


if __name__ == "__main__" :
    main2()
    #check()
