""" #####################################################
発想


##################################################### """
def cheaker() :
    """ 実は初期設定のA内の10要素だけを実装するのではなく、追加された変数もお仕事する関数 
    
    Aないの使用していない要素が無くなるまで実行するてきなニュアンスかな。
    処理が収束しない可能性があるため、使用には注意が必要
    """
    A = list(range(10))
    i = 0
    for a in A :
        i += 1
        if i % 3 == 0 :
            A.append(a)
        print(a)    
    return


def main() :
    return


if __name__ == "__main__" :
    #main()
    cheaker()
