import random
import datetime
import GameSystem

def Main():
    print("こんにちわ")
    print("今日は{}日です".format(datetime.date.today()))
    print("")
    MainMenu()

def MainMenu() :
    Vocabulary = GameSystem.Vocabulary()
    Mode = ModeSystem()
    PlayerData = GameSystem.PlayerData()
    
    while True :
        print("")
        print("MainMenu-----------------------------------")
        print("何をするか指定してください")
        print("単語で遊ぶ⇒[z]+[enter]")
        print("単語の追加⇒[a]+[enter]")
        print("単語の編集⇒[e]+[enter]")
        print("終了⇒[x]+[enter]")
        print("cheak⇒[c]+[enter]")
        print("")
        mode = input("入力：")

        if mode == "z" :
            Mode.gamemode(Vocabulary,PlayerData)
        elif mode == "a" :
            Mode.addmode(Vocabulary,PlayerData)
            break
        elif mode == "e" :
            Mode.editmode(Vocabulary,PlayerData)
            break
        elif mode == "x" :
            Mode.exitmode(Vocabulary,PlayerData)
            break
        elif mode == "c" :
            Mode.cheak(Vocabulary)
            break
        else :
            print("何してる！？入力しなおしてもろて")

    #情報の更新
    MainMenu()
    return

class ModeSystem :
    def Savemode(self,Vocabulary,PlayerData):
        print("")
        print("****************************************")
        print("新単語とPlayerDataを保存します")
        Vocabulary.SaveFile()
        PlayerData.LibraryUpdater(Vocabulary.vocabulary)
        PlayerData.SaveFile()
        print("")
        print("保存が完了しました")
        print("****************************************")
        return
    
    def gamemode(self,Vocabulary,PlayerData) :
        print("")
        print("GameMode----------------------------")
        print("")
        print("苦手克服モードを使用しますか？")
        weakness = input("はい:enter/いいえ:any key enter") 
        print("")
        Tryint = int(input("何回遊びますか？："))
        count = 0
        for i in range(Tryint) :
            print("")
            print("")
            print("")
            print("######################################")
            print("第{}問目！".format(i+1))
            num = random.randint(0,len(Vocabulary.vocabulary)-1)
            v = Vocabulary.vocabulary[num]
            if not weakness :
                while v[0] in PlayerData.learned_words :
                    num = random.randint(0,len(Vocabulary.vocabulary)-1)
                    v = Vocabulary.vocabulary[num]
            Q = GameSystem.Question(v[0],v[1],v[2],v[3],v[4])
            #DebugLog(Q)
            memory_statue = Q.Execute()
            PlayerData.WritingTheResults(v[0],memory_statue)
            count += self.Result(memory_statue)

        print("")
        print("")
        print("終了！")
        print("{}問中{}個正解でした".format(i+1,count))
        print("")
        print("")
        print("修正したい文字はありましたか？")
        print("ある⇒文字/ない⇒enter")
        string = input("入力：")
        while string :
            Vocabulary.AmendVocabulary(string)
            print("")
            print("まだある⇒文字/もうない⇒enter")
            string = input("入力：")

        self.Savemode(Vocabulary,PlayerData)
        
        print("")
        print("もっと遊ぶ？")
        print("やる！⇒enter/終わり⇒press any key")
        if not input("入力：") :
            self.gamemode(Vocabulary,PlayerData)
            return
        
        print("")
        input("Please press any key to exit")
        
    
    def Result(self,memory_statue) :
        if memory_statue == "collect" :
            return 1
        else :
            return 0
            
    def addmode(self,Vocabulary,PlayerData) :
        Vocabulary.AddVocabulary()
        self.Savemode(Vocabulary,PlayerData)
        return

    def editmode(self,Vocabulary,PlayerData) :
        print("修正したい文字を教えて下さい")
        print("")
        string = input("word：")
        while string :
            Vocabulary.AmendVocabulary(string)
            print("")
            print("まだある⇒文字/もうない⇒enter")
            string = input("入力：")
        print("")
        print("追加しました。")

        self.Savemode(Vocabulary,PlayerData)

        print("MainMenuに戻ります")
        return

    def exitmode(self,Vocabulary,PlayerData) :
        self.Savemode(Vocabulary,PlayerData)
        
        mode = input("ほんとに終了する？終了⇒enter")
        if not mode :
            exit()
        else :
            return
        
    def cheak(self,Vocabulary) :
        for i in range(len(Vocabulary.vocabulary)):
            print("ワード名{}の確認をします。".format(Vocabulary.vocabulary[i][0]))
            for j in range(len(Vocabulary.vocabulary[i])) :
                print(Vocabulary.vocabulary[i][j])
            
def DebugLog(Q) :
    print("")
    print("Q.word⇒{}".format(Q.word))
    print("Q.mean1⇒{}".format(Q.means[0]))
    print("Q.hint1⇒{}".format(Q.hints[0]))
    input("処理を続けます")

if __name__ == "__main__":
    Main()
    

