import datetime
import os

###############################################################
#競技プログラム問題用の、
#pyフォルダとファイルを生成するプログラム

#フォルダ内に既存のファイルがある場合
#何も処理しないので注意。

###############################################################
#解答を記載するプログラムに書いておく内容
def mypy() :
    write_str = ['def checker() :',
                 '    return',
                 '',
                 '',
                 'def main() :',
                 '    return',
                 '',
                 '',
                 'if __name__ == "__main__" :',
                 '    main()',
                 '    #checker()']
    #改行の挿入
    for i in range(len(write_str)) :
        write_str[i] = write_str[i] + "\n"

    return write_str

#ファイル作成(python)を行う関数
def makefile(Newfilename, writeList = None) :
    for i in Newfilename :
        with open(i , mode="w",encoding = "UTF-8") as f :
            if not os.path.isdir(i) :
                f.write("")
                if writeList :
                    f.writelines(writeList)

def main() :
    #作りたいファイル名指定
    mypyName = [f"{i}" for i in range(5) ]
    #anspyName = ["C-Ans","D-Ans","E-Ans"]
    Date = str(datetime.date.today())

    #フォルダ名、ファイル名の作成
    Newdirname = os.path.join("./",Date)
    Newfilename_my = [os.path.join(Newdirname , name + ".py") for name in mypyName]
    #Newfilename_ans = [os.path.join(Newdirname , name + ".py") for name in anspyName]

    #フォルダ作成
    os.makedirs(Newdirname,exist_ok=True)

    #ファイル作成
    makefile(Newfilename_my ,mypy())
    #makefile(Newfilename_ans)
    
if __name__ == "__main__" :
    main()














def memo() :

    """
    以下はプログラミングにおける知識のメモ

    Memoname = "MEMO.txt"
    #ファイル作成（txt）
    with open(Memoname,mode="w",encoding = "UTF-8") as f :
        if not os.path.isdir(Memoname) :
            f.write("")
    """


    """
    b = os.path.join("./","S.py")
    a = os.path.join(os.path.abspath(os.path.dirname(__file__)),"S.py")
    c = os.path.join(os.path.dirname(__file__),"S.py")
    print(a)
    print(b)
    print(c)


    print("join(): " + os.path.join("/A/B/C", "file.py"))


    os.path.join の使い方。
    二つのpathの名前を結合して一つのパスにすることができる。
    （pathの取得、生成）というやつですな
    abspath⇒絶対パス
    dirname⇒今使用しているパスの名前。（相対パス）


    """
    #山岸20023042
    #機械力学の結果で聞いたはず。
