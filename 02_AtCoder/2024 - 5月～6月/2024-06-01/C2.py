""" #####################################################
竹田海渡の思うこと

仮にもしこの問題に対して正解することができていても、

全ての予想と合致しないパターンはどのように分けられるのか説明ができない
→難で動いているのかが分からない問題に直面すると思うんだが。






####################################################### """


def cheaker() :
    print(2**15)
    return


def checker2():
    """ 配列の最悪計算量 """
    a = 1
    for i in range(8, 16) :
        a *= i
    for i in range(1, 9) :
        a /= i
    print(a)
    # 6435.0 = 15C8
    return

def checker3() :
    """ binの挙動 """
    a = bin(10)[2:].zfill(8)
    print(a)
    return

def main() :
    N, M, K = map(int, input().split())
    
    #鍵の正しい数より、正しい本数がKのすべての考慮される事象を記した配列を作成する。
    convinations = []
    for n in range(2**N) :
        convi = bin(n)[2:].zfill(N) #長さNのバイナリー情報を作成する
        
        # 配列が正しいのかチェック
        key_count = 0
        for n2 in range(N) :
            if convi[n2] == "1" :
                key_count += 1
        
        if key_count == K :
            convinations.append(list(map(int, convi)))
        
    #状態のメモ
    convi_len = len(convinations)
        
    
    # 入力の判定
    for i in range(M) :
        strings = list(input().split()) #注意：全部stringとして入力する
        c = strings.pop(0)
        R = strings.pop()
        a = list(map(int, strings))
        c = int(c)
        
        # case0 入力が、keyより少ない場合は何もわからない
        if len(a) < K :
            continue
        
        print("現在のconvinatinosはこれです")
        print(convinations)
        #case1 丸だった場合 →内蔵されている以外の数は必ずFalseになる
        if R == "o" :
            false_a = []
            for n in range(1, N+1) :
                if n not in a :
                    false_a.append(n)
            print("case1でした")
            print(f"現在の入力数値は{a}において、使わないことが確定した番号は{false_a}です")
            
            #違うことが確定している要素の削除工程
            for fa in false_a :
                i = 0
                while i < len(convinations) :
                    if convinations[i][fa-1] == 1 :
                        convinations.pop(i)
                    else :
                        i+=1
        
        #case2 R==xの時 入力された文字列分の場所が全てTrueの要素は削除可能
        else :
            i = 0
            while i < len(convinations) :
                #要素を抜き取る
                check_convi = []
                for j in range(c) :
                    check_convi.append(convinations[i][a[j]-1])
                print(f"現在の入力数値は{a}において、抜き題した配列は{check_convi}です")

                if all(check_convi):
                    convinations.pop(i)
                    print("抜き出しを行いました")
                else :
                    i+=1
         
    # 結果の出力           
    print(len(convinations))
   
    return

def checker4() :
    """配列調査"""
    a = ["0", "0", "1", "0"]
    b = list(map(int, a))
    print(b)


def checker5() :
    """ 配列調査２ """
    a = 1 << 10
    b = 4 << 10
    c = 10 >> 2
    d = 10 >> 4
    print(a)
    print(b)
    print(c)
    print(d)
    

if __name__ == "__main__" :
    #main()
    #checker2()
    #checker4()
    checker5()
    
    