""" #####################################################
発想

- 次の文字を選ぶ+ iを進める処理
- dream, erase は必ず使用するので、行けるなら確実にチェックする。
- (1)dream, (2)dreamer, (3)erase, (4)eraser としたとき
1. dなら 
    1. dreameraser 
    2. dreamerase
    3. dreamer
    4. dream 
    か判断し、e,dで始まるか判断する。    
2. eなら
    1. eraser
    2. erase
    か判断し、 e,dで始まるか判断する



...WAでした。
理由はわからん。
とりあえず別のアルゴリズムで挑戦することにする。

発想 aに着目。
全ての文字にaが格納されている。
er,rが無い状態の時、a周りがおけるかどうかの確認が必要だ。
er,rがある状態の時、erが含まれている場合とrが含まれている場合が存在するが、eraseに吸収されるケースも存在する。
eraseで吸収されるケースが存在する→eraseで検出済みなので、erの部分は上書きでOKにすると、全体カバーできそう。 rは頭文字が存在しないから+αで調査する必要があるね。

...WA
main1, main2 のWA数が一緒なので、同じコーナーケースを対応できていない。ということ。



...ACとれた!

解説おもしろい。dreamを逆から読んだらmaerdで、これは合致したら即座に取り除いて問題ない。ということである。



##################################################### """
def check() :
    return


def main() :
    S = input() + ("x"*12)
    #print(S)
    
    i = 0
    result = True
    while result and i < len(S)-12 :
        if S[i] == "d" :
            if "dreameraser" == S[i:i+11]:
                i += 11
                continue
            if "dreamerase" == S[i:i+10] :
                i += 1
                continue
            if "dreamer" == S[i:i+7] :#dreamの選択肢が無いため
                i += 7
                continue
            if "dream" == S[i:i+5]:#ラストの可能性
                i += 5 
                continue

        elif S[i] == "e" :
            if "eraser" == S[i:i+6] :
                i += 6 
                continue
            if "erase" == S[i:i+5] :
                i += 5 
                continue
        result = False

    if result and i==len(S)-12 :
        print("YES")
    else :
        print("NO")
    return

def main2() :
    S = "x"*5 + input() + "x"*5
    R = [0]*5 + [1]*(len(S)-10) + [0]*5 

    for i,s in enumerate(S) :
        if s == "a" :
            if S[i+1] == "m" :
                if S[i-3:i] == "dre" :
                    for j in range(-3, 2): R[i+j] = 0 
                    if S[i+2:i+4] == "er" :
                        for j in range(2, 4) :R[i+j] = 0
            elif S[i+1] == "s" :
                if S[i-2:i] == "er" and S[i+2] == "e" :
                    for j in range(-2, 3): R[i+j] = 0
                    if S[i+3] == "r" : R[i+3] = 0
        
    #print(R)
    if sum(R) > 0 :
        print("NO")
    else :
        print("YES")

if __name__ == "__main__" :
    main2()
    #check()
