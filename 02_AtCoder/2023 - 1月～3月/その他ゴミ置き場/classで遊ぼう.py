"""
##メソッド⇒（class ）def---　の関数のこと

class TestClass :
    x = "変数１"
    y = 5
    z = [4]

    def test_method1(self) :
        print(self.x)

    def test_method2(self,arg1) :
        print("引数1:"+ arg1)

    def test_method3(self) :
        print(self.y)
        for i in range(self.y) :
            self.z.append(i)
        print(*self.z)

testClass = TestClass()
testClass.test_method1()
testClass.test_method2("引数Test")
testClass.test_method3()


"""



from collections import deque

#なぜか前の方で定義しないといけない変数たち。
N = 3
a = 2

class Graharg(N) :
    #クラス定義で設計される形。
    n = [-1 for i in range(N)]
    que = deque()
    G = []
    
    #for i in range(a) :
    #    G.append([input().split()])

    def __init__(self) :#コンストラクタの定義 初期化
        return

    def __del__(self) :#デストラクタ　
        print("del:デストラクタ")
        """
        インスタンスの削除のさいに呼び出される
        例
        　del Graharg
        の時
        """
        
    def BFS(self) :
        count = 0
        while count < self.N :
            count += 1
            print("..BFS..")

        return count

    def DFS(self) :
        print("DFS")
        return
    


b = Graharg(N)

#a.DFS()









    
