""" 霧雨魔理沙を助けるゲーム

https://sairoutine.github.io/MARISA-HighLow/public/

一回きり、

やれること。

ハイスコア、
成功確率の定義。

- ハイスコア
    - sameを最大回数当てつつ、
    lowhighを必ず成功させれば、ハイスコアになる。
    - 理論上のハイスコア
    = 10**10 * 2**8 = 

# Gameクリアをするのに必要な条件。
- 1億円ゲットすること。 1億= 10**8 
- ...27回成功させる必要がある。



...さて、
現状queryにおいて、何のアクションをとったら、
一番成功確率が高くなるのだろうか???という問題を解きたい。

めくれる順番は残り
35!
である。これを全数調査するのは無理。
- これは概算だが、25回10以上の数値を乗算するので、最低10**25となる。
競技プログラミングで与えらているコンピュータの単位時間当たりの処理回数が(1秒につき)10**9であるため
10**16秒は最低かかる。すると愚直に計算しようとすると2億7千万年かかってしまうね。

# 問題の再定義
- 魔理沙さんが死ぬ確率を抑えたい。
→失敗する回数を最小限にするためにはどうしたらいいのか?


## 問題を最小単位で考える。
- とりあえず、選べるカードが
    - 赤のみ, 現在7番がめくれている, 残り8枚めくることができ、
    の 27/4, 7,6回成功するために必要な確率を求めることとしよう。
- 現在における、カードのめくれる先というのは...
    - 6/8 で下、2/8 で上になる。
    - 下を選択した場合、6/8でお金が増え、残り回数が1回減る。
    - 

- 小さい範囲の時、めくれる通りは、8!通りなので、全数で列挙可能。
1-2-3-4-5-6-8-9 = d-u-u-u-u-u-u-u-u
1-2-3-4-5-6-9-8 = d-u-u-u-u-u-u-u-d
1-2-3-4-5-8-9-6 = d-u-u-u-u-u-u-u-d
1-2-3-4-5-8-6-9 = d-u-u-u-u-u-u-d-u
1-2-3-4-5-9-8-6 = d-u-u-u-u-u-u-d-d
1-2-3-4-5-9-6-8 = d-u-u-u-u-u-u-d-u
...
...
シミュレーターなので、初動が7だった時、めくれるカードの順番は、
u,d どのような構成になるのだろうか数え上げてみる。
uの最大数が7なので、uが出る回数をindexとしたcountを作ってみる

...シミュレータが完成した。
とりあえず、次の9枚のうち、総計のうちどれくらいupdownの分布があるのかを調査することができる。


.. だが、本当に知りたいこととは違う。
出すべき答えは、
序盤に high lowを当きった方がいいのか、
passを序盤から有効活用して目指した方がいいのか。ということ。

これを出すためには、
序盤passを使用した場合と、終盤passを使用した場合の成功確率を出すべき。


...追加の問題前提として、
現在カード番号が cで
c以下のカード枚数 > c以上のカード枚数: 必ずc以下を選んだ方が良い結果になる。これを自明とする。
c以下のカード枚数 < c以上のカード枚数: c以上を選ぶ
c以下のカード枚数 = c以上のカード枚数: 1/2で上、1/2でしたを選ぶ。

...??
これは、どれだけ、失敗確率を減らすかということ。
つまり、取得できる失敗確率の総和を最小にするか????という問題である。
小さい単位で考えたとき
    c以下のカード枚数 = c以上のカード枚数: なら失敗確率が最大の1/2になるためpassすればよい。

理想的には、
35! 通りの選び方を全列挙し、
成功確率のヒストグラム(0%失敗~最大50%失敗)を見て、passができる面積分だけヒストグラムの上部から削除していけばよさそう。
上部から削除するといっても、めくる順番が未知で、複数の確率の合算ヒストグラムなので確定できんが。
...一つ分かったこと。
この問題は結果を一意に定めることが難しそうである。
ではできること。最適解を導出することを目指した方がいいのでは???


...?
あと、この問題の肝→同じ番号がめくれる可能性があるということ。
序盤こそ失敗確率が大きすぎる。だから、序盤は選ぶことは推奨されないが、
中盤である程度確率を絞ることができたとき大きく戦略変わるだろう。

参考
    sameを0回当てるなら、合計27回成功させればよい。(highlowの回数は27)
    sameを1回当てるなら、合計25回成功させればよい。(highlowの回数は24)
    sameを2回当てるなら、合計22回成功させればよい。(highlowの回数は20)
    sameを3回当てるなら、合計20回成功させればよい。(highlowの回数は17)
    sameを4回当てるなら、合計18回成功させればよい。(highlowの回数は14)
    sameを5回当てるなら、合計15回成功させればよい。(highlowの回数は10)
    sameを6回当てるなら、合計13回成功させればよい。(highlowの回数は7)
    sameを7回当てるなら、合計11回成功させればよい。(highlowの回数は4)
    sameを8回当てるなら、合計8回成功させればよい。(highlowの回数は0)


- 1回当てると、1/2を当てなければならない回数が最低3回は減る。
- 確率分布が大きいのはsameを当てる2回目,5回目,8回目→1/2を当てる必要がある可能性が4回減る。
- 1/1~1/2を3回当てるのと、1/1~1/9を挑戦して得られるメリットを増やすのはどっちがいい?????????

- マジわからん。決め打ち1/3とする? 
    - 決め打ち戦略
        - high-low 上が1,下1,same1だった時、成功確率1/3, 死亡1/3, スルー1/3 or 成功確率1/3+後続の死亡確率回収, 死亡2/3 
        この時は、もう感覚的で悔しいが、sameを狙った方が良い。

- せっかくシミュレータを作った。

残り35枚で、現在6/9 で成功、2/9で失敗する可能性がある。
これは、挑戦権がある確率なのか知りたい。

その方法として、
成功確率が0~B~100%になる回数はどれくらいあるのかを格納するリスト

計算量 35回選ばれる(初期条件は必ず赤の7) 
残っている枚数のうち、多いほうが出る確率 を取得。

ただし、最初～中盤、終盤で大きく確率が変わると思われる。
- 35~20までの成功確率分布、
- 20~10までの成功確率分布、
- 10~1までの成功確率分布
それぞれ算出することにする。


- simurationをするにあたって、
どの配列が使用されたのかをメモして保持しておくクラスが必要である。


"""
import os
import time
from datetime import datetime
import random
from collections import defaultdict
import itertools

def main() :
    """ 本番プログラム

    進捗状況を保持して、次の勝率をひとつづつ確認できるmainプログラム 
    """
    game = myCards()

    for i in range(34) :
        # 勝率を計算する
        win_per = game.get_success_probability()
        print("//////////////////////////////////")
        print(f"現在の勝率: {win_per}")
        print()

        # 次の値を格納する
        input("行動を選択しましょう。※推奨:勝率60%、勝率67%以上の時選択")
        flag_ok_input = False
        while flag_ok_input == False :
            next_color = int(input("次の色はなんですか? (colorはred=0, blue=1, green=2, pink=3のように入力する)"))
            number = int(input("めくれた番号を入力してください"))
            print("----------------------------------------------")
            print("入力は以上で大丈夫ですか?")
            print(f"色: [ {next_color} ] (colorはred=0, blue=1, green=2, pink=3)")
            print(f"番号: [ {number} ]")
            print("----------------------------------------------")
            _tmp_flag = input("OKなら「Enter」だけ")
            if _tmp_flag : continue
            else :
                flag_ok_input = True
        
        # 次の値へ更新する
        game.flip_card_handle(next_color, number)

    print("ラストです")
    win_per = game.get_success_probability()
    print("//////////////////////////////////")
    print(f"現在の勝率: {win_per}")
    input("plase enter")
    print("お疲れさまでした。")





    return







def check_day_time() :
    day_time = 60*60*24
    print(day_time)
    print(len(str(day_time)))
    print(10**11/365)

def check_high_score() :
    """ 理論上のハイスコア 
    
    1. same x3 当てる、 =10**3
    2. high row 当てる =2
    3. 1当てる = 10**3
    4. 2~3を繰り返す。（合計8回）

    - result 
        - 1* 10**3 *(2*10**3)**8
    """
    result = 1* 10**3 *(2*10**3)**8
    print(f"result:{result}, len:{len(str(result))}")
    return

def check_ac_count_for_game_crear():
    """ Game達成に必要な最低の成功回数について 
    
    1 から10**8を超えるまでの回数
    = 27回成功させなければならない。
    = 4*9-1 = 35回、
    
    全てHighlowで当てていく(sameを使わない)場合、
    **passは8回まで**しか使うことができないことになる。

    では、sameをn回当てる(最大8回)当てた際の、必要回数は???
    playできる合計回数は35回です
    sameを0回当てるなら、合計27回成功させればよい。(highlowの回数は27)
    sameを1回当てるなら、合計25回成功させればよい。(highlowの回数は24)
    sameを2回当てるなら、合計22回成功させればよい。(highlowの回数は20)
    sameを3回当てるなら、合計20回成功させればよい。(highlowの回数は17)
    sameを4回当てるなら、合計18回成功させればよい。(highlowの回数は14)
    sameを5回当てるなら、合計15回成功させればよい。(highlowの回数は10)
    sameを6回当てるなら、合計13回成功させればよい。(highlowの回数は7)
    sameを7回当てるなら、合計11回成功させればよい。(highlowの回数は4)
    sameを8回当てるなら、合計8回成功させればよい。(highlowの回数は0)
    """
    print(f"playできる合計回数は{4*9-1}回です")
    for i in range(9) :
        money = 10**i
        result = high_low_counter(money) + i
        print(f"sameを{i}回当てるなら、合計{result}回成功させればよい。(highlowの回数は{result-i})")
    return


def simurate_probability() :
    """ ある地点の成功確率がdefaltdict(key)であるときの、立った総回数 
    
    
    Note
    ------------------------
    残り35枚で、現在6/9 で成功、2/9で失敗する可能性がある。
    これは、挑戦権がある確率なのか知りたい。

    その方法として、
    成功確率が0~B~100%になる回数はどれくらいあるのかを格納するリスト

    計算量 35回選ばれる(初期条件は必ず赤の7) 
    残っている枚数のうち、多いほうが出る確率 を取得。

    ただし、最初～中盤、終盤で大きく確率が変わると思われる。
    - 35~20までの成功確率分布、
    - 20~10までの成功確率分布、
    - 10~1までの成功確率分布
    それぞれ算出することにする。

    Note2
    ---------------------------
    - シミュレーション計算量
        - 1回のシミュレーションにかかる所要時間
        1. 35回の探索(K)
        2. 確率の計算 O(M)
        3. 次の移動先決定 O(M)
        以上より、1回のシミュレーションにかかる計算量= O(K(M+M)) 
        ひどく見積もって、O(KM)< 10**3くらいかな???
        - 以上より、繰り返し回数Nは
            - 10**5くらいまでは1秒以内で作業が完了しそう。
    """
    N = 10**5 #シミュレーション回数

    # シミュレーションの開始    
    _now_time = time.time()
    beginning, middle, final = defaultdict(int), defaultdict(int), defaultdict(int)# 各時間帯における確率表を記載する辞書 序盤,中盤,終盤の意味
    for n in range(N) :
        tmp_game = myCards()
        
        # 序盤の計算
        for i in range(15) :
            _p = round(tmp_game.get_success_probability()*100, 3) #100分率%、少数以下3で取得
            beginning[_p] +=1
            tmp_game.filp_card()
        
        # 中盤の計算
        for i in range(10) :
            _p = round(tmp_game.get_success_probability()*100, 3) #100分率%、少数以下3で取得
            middle[_p] +=1
            tmp_game.filp_card()

        # 終盤の計算
        for i in range(9) :
            _p = round(tmp_game.get_success_probability()*100, 3) #100分率%、少数以下3で取得
            final[_p] +=1
            tmp_game.filp_card()
        _p = round(tmp_game.get_success_probability()*100, 3) #100分率%、少数以下3で取得
        final[_p] +=1

    # シミュレーション結果の整理 1. 成功率の正規化と、累積分布関数の導出
    def _caluclate_cdf_and_probability(probability_frequency:dict) :
        """ 集計結果の確率分布から、その地点における全体の割合と累積和を導出する 
        
        Parameters
        ----------------
        - probability_frequency: defaltdict (key,value)
            - keyがある地点からカードをめくるときの成功確率(試行方法はfileの全体ドキュメントを参照)
            - valueは、その地点の成功確率に面した回数
        
        Returns
        --------------
        - normalized_probability_frequency : defaltdict(key,value)
            - 入力のcountが0~1の確率になった辞書型変数
        - cdf: defaltdict(key,value)
            - 入力の辞書を最小key順に並べたとき、その累積度(0~1) 
        """
        if not isinstance(probability_frequency, defaultdict):
            raise TypeError("入力の型が違います")
        if not probability_frequency:
            raise ValueError("入力辞書の中に何も入ってません")
        
        count_sum = sum(probability_frequency.values())
        normalized_probability_frequency = defaultdict(float)
        cdf = defaultdict(float)

        current = count_sum
        for key in sorted(probability_frequency.keys()) :
            normalized_probability_frequency[key] = round(probability_frequency[key]/count_sum, 3)
            cdf[key] = round(current/count_sum, 3)
            current -= probability_frequency[key]   
        
        return normalized_probability_frequency, cdf
    beg_n, beg_cdf = _caluclate_cdf_and_probability(beginning)
    mid_n, mid_cdf = _caluclate_cdf_and_probability(middle)
    fin_n, fin_cdf = _caluclate_cdf_and_probability(final)

    # シミュレーション結果の出力
    current_time = datetime.now().strftime('%Y-%m-%d-%H-%M')
    common_dir_name = os.path.join(os.path.dirname(__file__), f"result-{current_time}")
    if not os.path.exists(common_dir_name):
        os.makedirs(common_dir_name)
    with open(os.path.join(common_dir_name,"beginning.txt"), 'w') as file:
        # defaultdict のキーと値を一行ずつ書き込む
        file.write("直面回数\n")
        for key in sorted(beginning.keys()):
            file.write(f"{key}: {beginning[key]}\n")
        file.write("\n\n")
        file.write("直面回数の割合\n")
        for key in sorted(beg_n.keys()):
            file.write(f"{key}: {beg_n[key]}\n")
        file.write("\n\n")
        file.write("累積分布\n")
        for key in sorted(beg_cdf.keys()):
            file.write(f"{key}: {beg_cdf[key]}\n")

    with open(os.path.join(common_dir_name,"middle.txt"), 'w') as file:
        # defaultdict のキーと値を一行ずつ書き込む
        file.write("直面回数\n")
        for key in sorted(middle.keys()):
            file.write(f"{key}: {middle[key]}\n")
        file.write("\n\n")
        file.write("直面回数の割合\n")
        for key in sorted(mid_n.keys()):
            file.write(f"{key}: {mid_n[key]}\n")
        file.write("\n\n")
        file.write("累積分布\n")
        for key in sorted(mid_cdf.keys()):
            file.write(f"{key}: {mid_cdf[key]}\n")

    with open(os.path.join(common_dir_name,"final.txt"), 'w') as file:
        # defaultdict のキーと値を一行ずつ書き込む
        file.write("直面回数\n")
        for key in sorted(final.keys()):
            file.write(f"{key}: {final[key]}\n")
        file.write("\n\n")
        file.write("直面回数の割合\n")
        for key in sorted(fin_n.keys()):
            file.write(f"{key}: {fin_n[key]}\n")
        file.write("\n\n")
        file.write("累積分布\n")
        for key in sorted(fin_cdf.keys()):
            file.write(f"{key}: {fin_cdf[key]}\n")
    
    print("処理を終了します")
    print(f"所要時間:{time.time()-_now_time}")
    return

def check_min_persent_for_win() :
    """ 勝たなければならない割合 
    
    0.7714285714285715
    77% の確率で勝利を勝ち取る必要がある、
    """
    print(28/35)
    print(25/35)

#################################
# utility
def high_low_counter(money) :
    """ 現在所持金がmoneyの時、残り全てをhighlowを成功させてクリアした場合に必要な試行回数を出力する関数
     
    Parameters
    ---------
    - money: int
        現在の所持金

    Return
    ---------
    - count: int
        10**8を超えるために必要な所持金
    """
    count = 0
    while money < 10**8:
        count +=1
        money = money*2
    return count

def simurate_small_ud_count(now_card_number:int=7, remaining_cards_list:list=[1,2,3,4,5,6,8,9]) :
    """ 全めくり方のうち、ある捜査の合計上昇回数がi回になるとき確率を 数え上げるシミュレータ

    Parametes
    -------------------
    - now_card_number: int
        - 現在めくれているカード番号
    - remaining_cards_list: list
        - 残っているカード番号をまとめたリスト。
    
    Return
    ------------------
    - console上に
        入力のカードをランダムにとっていって、
        ある捜査の合計上昇回数が i回になる確率を記したデータが出力される
        
    Note
    -------------------------------
    1色のみ、7始動、残り枚数8枚、
    8! のめくり方において、i
    見えたカード番号を格納する配列Aiがある。
    配列Aiにおいてj番目にめくれた数は Aij である。
    
    A(i)(j) < A(i)(j+1)であるとき、次にめくれた数は大きいことになりupしたので、upカウントをする。
    それ以外は数えない(downを数える)

    
    ..result
    ///////////////////////////////////////
    カードのめくれ方
    [0, 64, 2340, 12924, 17824, 6624, 540, 4]
    正規化(確率[%])
        0      1      2      3      4      5      6      7
    0.000  0.159  5.804 32.054 44.206 16.429  1.339  0.010]
    """
    # 入力チェック: 計算量的に、10枚以上の計算はできない。
    if len(remaining_cards_list) > 10 :
        raise ValueError("計算量オーバーします。10枚以下で入力してください")

    
    # Up downの数え上げアルゴリズム O(N!*N)
    card_permutations = list(itertools.permutations(remaining_cards_list)) #全順列
    up_counter = [0] *len(remaining_cards_list) #カードのめくり方を記した集合Aにおいて、8回のうちuがめくれた回数がiだった時の種類数を格納する配列
    for one_per in card_permutations:
        tmp_r = 1 if now_card_number < one_per[0] else 0 #1枚目めくったとき。
        for i in range(len(one_per)-1) :
            if one_per[i] < one_per[i+1] :
                tmp_r +=1
        up_counter[tmp_r] +=1
 
    # 正規化(確率表記)
    normalized_up_counter = [round(uc/len(card_permutations)*100, 3) for uc in up_counter]
    print("///////////////////////////////////////")
    print("カードのめくれ方")
    print(up_counter)
    print("正規化(確率[%])")
    print(" ".join(f"{i:>6}" for i in range(len(normalized_up_counter))))
    print(" ".join(f"{nuc:>6.3f}" for nuc in normalized_up_counter))
    return


class myCards:
    """ 現在の進捗状況を保持するクラス

    Parameters
    ------------------
    - start_cards: list(int, int) 
        - 開始状況を記載するリスト
        - [color, number] のように指定する。
        - colorはred=0, blue=1, green=2, pink=3のように入力する
        - numberはカード番号.
    """
    def __init__(self, start_cards=[0,7], next_card_color:int=2) :
        if not -1 < start_cards[0] < 4 or not 0 < start_cards[1] <10 :
            raise ValueError("クラス初期化の入力値が正常ではありません")
        elif not -1 < next_card_color < 4 :
            raise ValueError("クラス初期化の入力値が正常ではありません")
        
        self._cards = [[j for j in range(1,10)] for i in range(4)] 
        self._cards[start_cards[0]].remove(start_cards[1])
        self._now        = start_cards[1]  #現在の番号
        self._next_color = next_card_color #次の色

    def get_success_probability(self) :
        """ 次のカードめくりにおける成功確率を取得する関数 
        
        Note
        -----------
        - 成功確率
            - 多いほうの枚数/めくれるカードの総枚数
            - 多いほうの枚数 = max(self._now以下のすべての数値の合計枚数, self._nowより大きいの数値の合計枚数)
        - 計算量O(M)
        """
        higher_count, lower_count = 0,0
        for c in self._cards[self._next_color]: 
            if self._now > c:
                lower_count +=1
            elif self._now < c:
                higher_count +=1
        success_count = max(higher_count, lower_count)
        return success_count / len(self._cards[self._next_color])

    def filp_card(self) :
        """ 次のカードをめくる関数 計算量O(M) M:カードの残り枚数"""
        # 次の番号決定
        self._now = random.choice(self._cards[self._next_color])

        # 番号の抜き出し
        self._cards[self._next_color].remove(self._now)

        # 次の色定義
        self._next_color = random.randint(0,3)
        while len(self._cards[self._next_color]) == 0:
            self._next_color = random.randint(0,3)
            if not any(self._cards) : #もし要素が存在していない場合
                raise KeyError("もう_cardsに要素が存在しません")
        return
    
    def flip_card_handle(self, next_color:int, number:int) :
        """ カード情報を更新する """
        # 入力チェック
        if not -1 < next_color < 4 :
            raise ValueError("色が正常な値ではありません")
        elif not 0 < number < 10 :
            raise ValueError("番号が正常ではありません")

        # 番号の抜き出し
        self._now = number
        self._cards[self._next_color].remove(self._now)

        # 色の決定
        self._next_color = next_color
        return

if __name__ == "__main__" :
    main()
    #check_high_score()
    #check_ac_count_for_game_crear()
    #check_day_time()
    #simurate_small_ud_count()
    #simurate_probability()
    #check_min_persent_for_win()