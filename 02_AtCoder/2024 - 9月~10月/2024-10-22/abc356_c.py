""" #####################################################
発想

正解のカギの組み合わせ。

- if 入力がo 
    - 入力で× = は答えから除外できる。
- else 入力がx
    - 1101, 1011が存在する場合、in[3], in[2]はそれぞれ0, 1を検査している。
    これは、他が変わらなくて、この通りが存在する場合、3,2はそれぞれ必要な鍵であるといえる。
    - K=N-1 で、CaseでKだけ選択した場合、使用していない鍵が正解(確定)となる。
    つまり、testcase1 において、in[0]がTrueでないと間違いがわかった。→1がFalseの正解パターンは存在しない
    この検査は、undeterminedの配列要素数がnであるとき、
    K=n-1のテストケースがFalseなら、ひとつだけ確定する。ということ。

    注意:
    caseの要素数はC >K であるが、すでに不必要な鍵であると確定しているカギを使用している場合がある。検査するときは、確定したカギは削除しとかないとね。。


- flow
1. correct caseとincorrect caseを分ける。
correctcaseを全調査、xを確定する。

2. incorrect caseを全調査、
if len(undertermined) -1 == K であるときの検査



- 数え方。
すべての可能性から少しずつデータを減らす感じにしましょう。
全体 ans = 2**N

必要鍵or不必要鍵が確定した場合→ ans //2

いろいろ調査後、これ以上絞れない場合
残った可能性は間違っているということなので、
ans - 残った可能性の全数

あと、不必要な選び方
C < Kの時は、参考にならないということが言えそう。
だってどのような結果でも、必ずxになるから。

必要な鍵を検査する工程。
もし必要な鍵がわかったら、
Kの値を減らして、再度別の検証ができそう。
結果は、(N-len(incorrect_keys))comb K となるが、N-1かつ、K-1できそうである。

...鍵の位置は確定させなくてもいんじゃね?
もうcombinationの数から、ダメだったテストケースの数を引けば答えになりそう。

ただ、incorrect_caseの情報更新は必要。
削除した先で、もし検証すべきK以内の


ネック1.
N-len(incorrectkeys)のうち、ある一つを除くすべての要素が1であり、xという結果の時
→0の要素は必ず必要→大きく絞れる。

ネック2.
ダメな例の数え上げ、
0000111100 
N=10, K=3の時、
この際、どんなに頑張っても
0000111100
----0001--
----0010--
....
----1110--
がTrueになることはない。→大きく減らすことができる。
x以下に存在するすべての可能性は、必ずFalseになる。絞れる。
ネック1と似ているが、それ以上1を0にした配列は、必ず間違いだよと言い切ることができるということ。




##################################################### """
def check() :
    return

from itertools import combinations
def main() :
    N, M, K = map(int, input().split())
    correct_case, incorrect_case = [], []
    for m in range(M) :
        In = list(input().split())
        if int(In[0]) < K : continue #どんな選び方でもxなものは参考にならないものとする。 
        if In[-1] ==  "o" :
            correct_case.append(In[:-1])
        else :
            incorrect_case.append(In[:-1])

    
    keys = [-1 for i in range(N)] #鍵の確定状況
    # 1. 不必要な鍵の全調査
    for i in range(len(correct_case)) :
        tmp_key = [0 for n in range(N)]
        for j in range(int(correct_case[i][0])) :
            tmp_key[int(correct_case[i][j+1])-1] = 1
        for k in range(N) :
            if tmp_key[k] == 0 :
                keys[k] = 0
    
    # 2. 不必要な鍵を踏まえたうえで、配列の整理。 incorrect_keysは不必要と確定したカギ
    unknown_keys, incorrect_keys = [], [] 
    for i, k in enumerate(keys) : 
        if k == -1 : unknown_keys.append(i+1)
        else : incorrect_keys.append(i+1)
    #result = 2**(N-len(incorrect_keys)) #鍵の選び方。
    #print(unknown_keys)
    #print(incorrect_keys)

    if K > N - len(incorrect_keys) : #もし不必要な鍵が多すぎるとき、
        print(0) 
        return
    
    # 鍵でうまくいかなかったケースにおいて、残りの検証順にbitを作成しつつ、そのbitを10進数表記に直した値の生成。mをbitに直す
    new_incorrect_case = []
    for icc in incorrect_case :
        m = list(map(int, icc[1:]))
        m.sort()
        mi = 0
        tmp_incorrect_case = 0
        for j in range(len(unknown_keys)) :
            #print("-", unknown_keys[j], m)
            if unknown_keys[j] == m[mi] :
                tmp_incorrect_case += 2**j
                if mi < int(icc[0])-1 : mi += 1 
                else : break
        new_incorrect_case.append(tmp_incorrect_case)
    
    result = 0
    # bit全探索で、該当するkeyの数え上げを行う。2**N *M
    # ある組み合わせを定義、その組み合わせをM回だけ検証し、すべて問題なかったらresult+=1
    # ただし、定義したbitの1の総数がK未満である場合→無条件でFalse
    for bit in range(2**len(unknown_keys)) :
        active_bit_points = 0
        for i in range(len(unknown_keys)-1) :
            if bit & (1 << i) : #現在位置にbitが立っているか確認する
                active_bit_points += 1
        if active_bit_points < K : #そもそもbitの総数が足りない。
            continue
        
        r = True
        for m in new_incorrect_case : #あるbitに対して、すべてのincorrect_caseを実行し、可能性としてありうるならTrueを、必ずxになるなら、Falseを
            if bit & ~m == 0 : 
                r = False
                print(bit)
                break
        result += r
        #print(f"test_caseのbit{bit}, bit_2_{format(bit, f'0{len(incorrect_keys)}b')}は、どのFailcaseも参考になりませんでした")
    print(result)
    return


if __name__ == "__main__" :
    main()
    #check()
