""" 部分文字列の列挙を用いる問題。便利配列のライブラリ 


部分文字列問題。
ある任意の文字列my_s を作成で最初に到達できる番号を返すライブラリ。
class mySubString(str) :
    def get_next_substring_index(c:str, x:int):
"""

class mySubString :
    """ mode=0で 0~9, mode=1で a~zの便利配列を作成します。"""
    def __init__(self, s:str, N:int=-1, mode:int=0) :
        self.N = N if N != -1 else len(s)
        self.S = s
        self.mode = mode#0が 0~9の番号。 1でa~z のアルファベット

        # 便利配列の作成
        if mode == 0 : #番号モードの時
            self.next_i_substrings = [[-1 for j in range(10)] for i in range(self.N+1)]
            for i in range(self.N, 0, -1) :
                for j in range(10): self.next_i_substrings[i-1][j] = self.next_i_substrings[i][j]
                self.next_i_substrings[i-1][int(self.S[i-1])] = i #現在着目している文字の位置
        elif mode == 1 : #アルファベットmodeの時
            self.next_i_substrings = [[-1 for j in range(26)] for i in range(self.N+1)]
            for i in range(self.N, 0, -1) :
                for j in range(26): self.next_i_substrings[i-1][j] = self.next_i_substrings[i][j]
                self.next_i_substrings[i-1][ord(self.S[i-1])-ord("A")] = i #現在着目している文字の位置
        else :
            raise ValueError("便利配列の形式が文字列や数字ではないため、クラスが定義できません")
        
    def get_next_i(self, c, x:int) :
        """ 現在位置x より後で文字列or数字cが現れる最も最初の位置を返す関数

        Parameters
        -----------
        - c : str or int
            見つけたいオブジェクト
            ※一つずつ指定すること。
        - x : int
            調査を開始したい位置。1~N で文字の何番目か

        Returns
        -----------
        1. cの型とmodeの型が違うとき、Errorを出力します。
        2. xより後のindexで調査obj cが現れない場合は-1を返します。
        3. 見つけたら、1~N でのindexを返します。 
        """
        if self.mode == 0 and isinstance(c, str) : raise ValueError("modeが0~9です。文字列を入力してはいけません。")
        elif self.mode == 0 :
            return self.next_i_substrings[x][c]
        else:
            return self.next_i_substrings[x][ord(c)-ord("A")]
