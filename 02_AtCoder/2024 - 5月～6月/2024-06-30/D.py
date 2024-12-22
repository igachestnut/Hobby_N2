

""" 
def cheaker() :
    return
    
発想

# 識別番号の設定
- 右進む軍隊 right_*
- 左に進む軍隊 left_*
    
## 流れ
1. 右に進んだありに着目
2. 開始前で、右に位置する、最も近い左に進みたいありの番号を知る=(1)
3. 終了後、左に位置する、最も近いアリの番号をしる=(2)
4. そのアリがすれ違った回数= (2)-(1)である




"""
def main() :
    N, T = map(int, input().split()) #N=アリの数, T=経過時間
    S = list(input())
    X = list(map(int, input().split()))
    
    #距離順にソート
    ant_positions = {x : s for x, s in zip(X,S)}
    print(ant_positions)
    
    #情報整理・右に進むものと、番号の調査#右に進みたい(正方向に進む)アリの調査
    right_ant,left_ant = [], []
    for key, value in ant_positions.items() :
        if value == "1" :
            right_ant.append(int(key))
        else :
            left_ant.append(int(key))
    print("---")
    print(right_ant)
    print("--")
    print(left_ant)
        
    #T時間経過した状態の計算
    after_X = []
    for i in range(N) :
        if S[i] == "0" :#アリが負の方向を見ている
            after_X.append(X[i]-T)
        else :
            after_X.append(X[i]+T)
    #print(after_X)
    

if __name__ == "__main__" :
    main()
    #cheaker()

