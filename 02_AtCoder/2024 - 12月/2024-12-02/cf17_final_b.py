""" #####################################################
発想


- S<10**5
- 2文字以上の回文がないか査定する。
- 必ず回文になる可能性
    - aba aab だめ。2つ以上の文字列が並ぶ。3文字が違くない
    - aaabbbccc abcabcabc OK 
    - 文字は隣り合ってはいけない。i,i+2の文字列が同じであってはいけない。

- |S|=1の時、必ずTrue
- |S|=2の時、1種類=False, 2種類True
- |S|=3の時、1種類=False, 2種類False, 3種類=True
- |S|=4の時、1種類=False, 2種類False, 3種類=True(abca)
- |S|=5の時、1種類=False, 2種類False, 3種類
    - abcab 2,2,1 = True
    - ほか  3,1,1 =False

    - |S|-3種類(1,1,1を差分)した時、残ったもの が2種類以上ならTrue。

- どれだけオブジェクトを異なる3種類の1,1,1で抜き出せるか。
- そして、抜き出し方が適切でないと、答えが間違うことになる。
    3,3,3,2 の時 2を残すとFalseになるが、1,1とのコストTrueになる。

- 最も大きく含まれているアルファベットを優先的に抜き出して, |S|<=3になるまで実行する。

多分だけど、異なる3種類のアルファベットが抜かれたとき、
それぞれ独立に考えることができそう。
abc, abd なら、abcabdと置けばいいし
abc, abd, abd なら abc,abd,abd これで回文はない。適当で大丈夫そうである。

- アルファベットの数をソートして表現すると、
    0,0,,,1 2 3 4,8,9 のようになるはず。
- アルファベットを3つずつ抜き出していくということなので、最も多いアルファベットの数がlen(S)/3 と同値の時。
    - |S| = 30, S[-1]=10の時、回文を抜き出していくとすべて,
    a**,a**,a** のようにいい感じにばらけてくれる。
    - |S| = 30, S[-1]=11の時、どれだけうまく分けても、ひとつは必ずaが2こ入ってしまう可能性がある。
    - |S| = 31, S[-1]=11の時、11この配列に分かれてくれるため...

- 結論
    if (len(S)+2)//3 >= sorted_alphabet_counts[-1] :
        True
    else:
        False

##################################################### """
def check() :
    #print(31/11)
    return


def main() :
    S = input()
    alphabet_counts = [0] *26
    for s in S: alphabet_counts[ord(s)-ord("a")] +=1
    alphabet_counts.sort()
    if (len(S)+2)//3 >= alphabet_counts[-1]:
        print("YES")
    else :
        print("NO")
    return

if __name__ == "__main__" :
    main()
    #check()
