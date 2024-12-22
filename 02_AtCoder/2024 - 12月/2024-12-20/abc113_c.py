""" #####################################################
発想

- 各市の識別番号を答えるやーつ
- 入力の市の設立年度はばらばらである。
- 出力は入力と同じ並びでお願い。

1. 設立年度の市順にしてね。
...

県: {year: 識別番号, year:,,}の辞書を作ることを目指す。

##################################################### """
def check() :
    a = "00000012"
    print(a[-6:])
    return

def main() :
    """ 辞書を使って解く
    autonomy_ID:自治体の識別番号を 県>設立年度>識別番号 で格納する二重辞書 
    prefecture: 県
    """
    N,M = map(int, input().split())
    autonomy_ID = dict()
    for i in range(N) : autonomy_ID[i+1] = dict()
    query = []
    for i in range(M) :
        p,y = map(int, input().split())
        autonomy_ID[p][y] = "0" #最初は全てID=0
        query.append([p,y])
    for prefecture, years in autonomy_ID.items() :
        new_years = dict()
        for i, y in enumerate(sorted(years.keys())) :
            p_id = "000000" + str(prefecture)
            y_id = "000000" + str(i+1)
            new_years[y] = p_id[-6:] + y_id[-6:]
        autonomy_ID[prefecture] = new_years
    
    for [p,y] in query :
        print(autonomy_ID[p][y])
    return


if __name__ == "__main__" :
    main()
    #check()
