#Vocabulary.txtを制御するファイル
import random
import datetime

class Vocabulary :
    def __init__(self) :
        #二次元配列
        self.vocabulary = self.OpenFile()
    
    def OpenFile(self) :
        WordList = []
        with open("Vocabulary.txt",mode="r",encoding="UTF-8") as f :
            for line in f :
                WordList.append(list(line.split(",")))
                #print("Debug:単語{}が読み込まれました".format(WordList[-1][0]))
        return WordList

    #上書き保存をする。（全て新しく書き出す）
    def SaveFile(self) :
        with open("Vocabulary.txt",mode="w",encoding="UTF-8") as f :
            for i in range(len(self.vocabulary)) :
                f.write(",".join(self.vocabulary[i]))
        return

    #新しい単語をpython側から追加する。
    def AddVocabulary(self) :
        print("")
        print("AddWordMode-------------------")
        while True :
            print("Please enter the new word")
            print("")
            AddWord = input("新しく追加したい単語を入力してください：")
            print("Duplicate cheak will be performed")
            if self.DuplicateChecker(AddWord) :
                self.CreateInfo(AddWord)
            print("")
            go = input("続けますか(続ける：enter。終了：何か入力)?/Would you like to continue?")
            if go :
                break
        print("Exiting AddWordMode-----------------")
        return
        
    def DuplicateChecker(self,_word) :
        for i in range(len(self.vocabulary)) :
            if (self.vocabulary[i][0] == _word) :
                print("既に追加されています/{} has been appended to vocabulary.txt".format(_word))
                return False
        print("「{}」という英単語を新しく作成します".format(_word))
        print("")
        return True

    def CreateInfo(self,newword) :
        info = []
        info.append(newword)
        info.append(input("mean："))
        info.append(input("hint1："))
        info.append(input("hint2："))
        info.append(input("hint3：")+"\n")
        while True :
            self.EditWordCheck(info)
            print("間違いはありませんか？")
            print("無い⇒enter/ある⇒anyKey")
            Input = input("入力：")
            if not Input :
                break
            else :
                info = self.Edit(info)
        self.vocabulary.append(info)

        
    def AmendVocabulary(self,editword) :
        print("")
        print("EditMode----------------")
        for i in range(len(self.vocabulary)) :
            if editword == self.vocabulary[i][0] :
                self.Edit(self.vocabulary[i])
                break
        else :
            print("ワード{}はなかったみたいでやんすね".format(editword))
        print("Exiting EditMode-------------")
        return

    #ワードの添削をして出力する関数
    def Edit(self,vocabulary) :
        print("")
        self.EditWordCheck(vocabulary)
        print("修正を開始します。どこを修正しますか？")
        print("word：「w」,mean「m」,hint:「h」,end：「null」")
        directive = input("入力：")
        
        while directive :
            print("「enter」だけなら変更しません")
            if directive == "w" or directive == "word":
                newstr = input("元word：{}⇒".format(vocabulary[0]))
                if newstr :
                    vocabulary[0] = newstr
            elif directive == "m" or directive == "mean":
                newstr = input("元mean：{}⇒".format(vocabulary[1]))
                if newstr :
                    vocabulary[1] = newstr
            elif directive == "h" or directive == "hint":
                newstr = input("元hint1：{}⇒".format(vocabulary[2]))
                if newstr :
                    vocabulary[2] = newstr
                newstr = input("元hint2：{}⇒".format(vocabulary[3]))
                if newstr :
                    vocabulary[3] = newstr
                newstr = input("元hint3：{}⇒".format(vocabulary[4]))
                if newstr :
                    vocabulary[4] = newstr
            else :
                print("無効なModeです。")
                
            print("どこ修正する？")
            print("word：「w」,mean「m」,hint:「h」,end：「null」")
            directive = input("入力：")

        print("修正を終了します")
        return vocabulary

    def EditWordCheck(self,info) :
        print("---------------------------")
        print("word：{}".format(info[0]))
        print("mean：{}".format(info[1]))
        print("hint1：{}".format(info[2]))
        print("hint2：{}".format(info[3]))
        print("hint3：{}".format(info[4]))
        print("---------------------------")

            
class Question :
    def __init__(self,_word,_mean="",_hint1="",_hint2="",_hint3=""):
        self.word = _word
        self.mean = _mean
        self.hints = [_hint1, _hint2, _hint3]

    def Execute(self):#問題を行うメソッド
        for i in range(4):
            ans = self.Input()
            if self.word == ans and i < 2 : 
                return self.Collect()
            elif self.word == ans :
                return self.Maybe()
            elif (i > 3) :
                return self.Faild()
            else :
                self.Retry(i)

    def Input(self) :
        print("")
        print("What is the English word that means '{}'?".format(self.mean))
        print("Write it in all lowercase letters.　(^^)_旦~~")
        print("")
        return input("入力：")
        
    def Collect(self) :
        print("------------------------------------")
        print("正解！やったね！")
        print("")
        print("https://chat.openai.com/?model=text-davinci-002-render")
        input("Please press any key to exit or next")
        return "collect"
    
    def Maybe(self) :
        print("------------------------------------")
        print("正解！あともうちょっと！")
        print("")
        print("https://chat.openai.com/?model=text-davinci-002-render")
        input("Please press any key to exit or next")
        return "maybe"
    
    def Retry(self,i):
        print("------------------------------------")
        print("不正解！")
        print("There may be a possibility of error or misspelling")
        print("Hint{}：{}".format(i+1,self.hints[i]))
        print("")
        _strings = ["再挑戦!","分かるかな?","頑張れ！","Never Give Up"]
        _index = random.randint(0,len(_strings)-1)
        print(_strings[_index])
        return 

    def Faild(self):
        print("------------------------------------------")
        print("残念!")
        print("")
        print("The collect answer is '{}'.　下記はChatGPTのURLです".format(self.word))
        print("https://chat.openai.com/?model=text-davinci-002-render")
        input("Please press any key to exit or next")
        return "incollect"
        
class PlayerData :
    def __init__(self) :                
        Data = self.OpenFile()
        #print(Data)
        self.login_days = self.Findint(Data,"ログイン日数：")
        self.last_login_day = self.Findstr(Data,"最終ログイン日：")
        self.try_count = self.Findint(Data,"全問題挑戦回数：")
        self.total_words = self.Findint(Data,"ライブラリに入っている単語数：")
        self.number_of_almost_memorized_words = self.Findint(Data,"もう少しで覚えそうな単語数：")
        self.number_of_words_already_memorized = self.Findint(Data,"覚えた単語数：")
        self.not_learned_words = self.Findset(Data,"もう少しで覚えそうな英単語：")
        self.learned_words = self.Findset(Data,"覚えた英単語：")      

        #self.DebugLogData()
         
        #最終ログイン日の判定
        Today = datetime.date.today()
        str_today = Today.strftime("%Y-%m-%d")
        if str_today != self.last_login_day :
            self.last_login_day = str_today
            self.login_days += 1
            
       
            
    def Findint(self,Data,path) :
        for i in range(len(Data)) :
            if path in Data[i] :
                Str = Data[i]
                return int(Str[len(path):-1])

    def Findstr(self,Data,path) :
        for i in range(len(Data)) :
            if path in Data[i] :
                Str = Data[i]
                return Str[len(path):-1]
                

    def Findset(self,Data,path) :
        for i in range(len(Data)) :
            if path in Data[i] :
                Str = Data[i]
                Strs = map(str,Str[len(path):-1].split(","))
                return set(Strs)
            
    def DebugLogData(self) :
        print("")
        print("DebugMode--------------------------------")
        print("ログイン日数：{}".format(self.login_days))
        print("最終ログイン日：{}".format(self.last_login_day))
        print("全問題挑戦回数：{}".format(self.try_count))
        print("ライブラリに入っている単語数：{}".format(self.total_words))
        print("もう少しで覚えそうな単語数：{}".format(self.number_of_almost_memorized_words))
        print("覚えた単語数：{}".format(self.number_of_words_already_memorized))
        print("もう少しで覚えそうな英単語：{}".format(self.not_learned_words))
        print("覚えた英単語：{}".format(self.learned_words))
        #print("ログイン日数：{}".format(self.login_days))
        #print("ログイン日数：{}".format(self.login_days))
        #print("ログイン日数：{}".format(self.login_days))
        input("Please press any key to next load")
        print("-------------------------------------------")

        
    def OpenFile(self) :
        Data = []
        with open("PlayerData.txt",mode="r",encoding="UTF-8") as f :
            for line in f :
                Data.append(line)
        return Data
    
    def SaveFile(self) :
        with open("PlayerData.txt",mode="w",encoding="UTF-8") as f :
            f.write("最終ログイン日：" + self.last_login_day + "\n")
            f.write("ログイン日数：" + str(self.login_days) + "\n")
            f.write("全問題挑戦回数：" + str(self.try_count) + "\n")
            f.write("\n")
            f.write("\n")
            f.write("ーーーーーーーーーーーーーーーーーーーーーーーーーー\n")
            f.write("ライブラリに入っている単語数：" + str(self.total_words) + "\n")
            f.write("もう少しで覚えそうな単語数：" + str(self.number_of_almost_memorized_words -1) + "\n")
            f.write("覚えた単語数：" + str(self.number_of_words_already_memorized -1) + "\n")
            f.write("\n")
            f.write("\n")
            f.write("ーーーーーーーーーーーーーーーーーーーーーーーーーー\n")
            f.write("もう少しで覚えそうな英単語：" + str(",".join(self.not_learned_words)) + "\n")
            f.write("\n")
            f.write("覚えた英単語：" + str(",".join(self.learned_words)) + "\n")
            f.write("\n")
            f.write("\n")
            f.write("ーーーーーーーーーーーーーーーーーーーーーーーーーー\n")
        return
    
    def LibraryUpdater(self,vocabulary) :
        self.total_words = len(vocabulary)
        self.number_of_almost_memorized_words = len(self.not_learned_words)
        self.number_of_words_already_memorized = len(self.learned_words)


    #結果を元にPlayerData情報を記入する関数
    def WritingTheResults(self,word,memory_status) :
        """
        word ⇒ 問題
        memory_status(記憶状況)⇒ collect , maybe , incollect
        """
        self.try_count += 1
        
        if memory_status == "collect" :
            self.MaybeSetRemove(word)
            self.CollectSetAppend(word)
        elif memory_status == "maybe" :
            self.MaybeSetAppend(word)
            self.CollectSetRemove(word)
        else :
            self.MaybeSetRemove(word)
            self.CollectSetRemove(word)
            
    def MaybeSetRemove(self,word) :
        if word in self.not_learned_words :
            self.not_learned_words.remove(word)
    def MaybeSetAppend(self,word) :
        if word not in self.not_learned_words :
            self.not_learned_words.add(word)
    def CollectSetRemove(self,word) :
        if word in self.learned_words :
            self.learned_words.remove(word)
    def CollectSetAppend(self,word) :
        if word not in self.not_learned_words :
            self.learned_words.add(word)

def Cheak() :
    import GameSystem
    PlayerData = GameSystem.PlayerData()
    print("デバッグ(PlayerDataに格納される文字列の確認を)します")
    print("-------------------------------")
    PlayerData.DebugLogData()
    return
      
if __name__ == "__main__":
   Cheak()
        
def MEMO() :
    """
    作りたいファイル構造
    　ボキャブラリーを情報取得し、リストに収める関数！⇒Vocabularyは二次元配列。
    　そのボキャブラリーを指定するだけで勝手に問題を出力する関数

    追加する関数
    　ワード検索
    　　mean1,mean2,mean3,hintsを入力していく
    編集する関数
    　ワード検索
    　　
    """
