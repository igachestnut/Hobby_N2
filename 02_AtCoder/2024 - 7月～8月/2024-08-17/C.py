def cheaker() :
    return


def main() :
    N, K = map(int, input().split())
    R = list(map(int, input().split()))
    
    #maxの組み合わせ = 5**8 なので全数調査
    def DFS(seq, i) :
        """現在のNodeから階下の候補を見つける 
        
        もし一番下の場合、条件チェックし、出力OKなら出力するだけ 
        
        Paramters
        -------------
        seq : list
            上階から渡された、現在のNodeリスト。
        i : int
            上階から渡される、現在のindex
        """
        if i == N :#次にNodeが存在しない場合。
            if sum(seq) % K == 0 :
                print(*seq)
            return
        
        #階下で候補の存在する分だけDFSの実行を行う。
        for r in range(1, R[i]+1) : 
            tmp_seq = seq + [r]
            DFS(tmp_seq, i+1)
    
    DFS([], 0)
    return



if __name__ == "__main__" :
    main()
    #cheaker()
