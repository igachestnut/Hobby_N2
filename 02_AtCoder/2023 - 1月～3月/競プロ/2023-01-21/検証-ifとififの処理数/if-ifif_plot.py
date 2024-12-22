import matplotlib.pyplot as plt
import time

###############################################################
#時間計算関数　出力は掛かった時間
def timecheaker(a,b,N) :#Nは乗数。10000程度かな
    #time1
    start = time.time()
    for _ in range(10^N) :
        if a==b :
            if b==a :
                pass
    time1 = time.time() - start

    #time2
    for _ in range(10^N) :
        if a :
            if b :
                pass
    time2 = time.time() - start - time1
    
    #time3
    for _ in range(10^N) :
        if a or b :
            pass

    time3 = time.time() - start - time2 - time1

    #time4
    for _ in range(10^N) :
        if a and b :
            pass

    time4 = time.time() - start - time3 - time2 - time1

    return time1,time2,time3,time4

#グラフ化関数
def Plot_show(x,ylist1,ylist2,ylist3,ylist4) :
    fig = plt.figure(constrained_layout = True)
    ax = fig.subplots()
    ax.plot(x,ylist1,label="{}".format("if== :if=="))
    ax.plot(x,ylist2,label="{}".format("if :if"))
    ax.plot(x,ylist3,label="{}".format("if or if"))
    ax.plot(x,ylist4,label="{}".format("if and if"))
    ax.set_title("if-ififの処理時間比較",fontfamily = "Yu Mincho")
    ax.set_xlabel("Count")
    ax.set_ylabel("time[s]")
    ax.legend()
    plt.show()
    return

#####################################################################
def main() :
    #if判定用データ
    a,b = True ,True
    N = 10000

    #時間計測(グラフデータ作成)
    x = list(range(100))
    T1_list,T2_list,T3_list,T4_list = [],[],[],[]
    for i in x :
        t1,t2,t3,t4 = timecheaker(a,b,N)
        T1_list.append(t1)
        T2_list.append(t2)
        T3_list.append(t3)
        T4_list.append(t4)

    #グラフ化（処理軽減のためいらない場合はコメントアウト）
    #Plot_show(x,T1_list,T2_list,T3_list,T4_list)
    
    #合計時間の出力
    t = [0 for _ in range(4)]
    t[0],t[1],t[2],t[3] = sum(T1_list),sum(T2_list),sum(T3_list),sum(T4_list)
    print("if== :if==での合計時間は{}[s]".format(t[0]))
    print("if :ifでの合計時間は{}[s]".format(t[1]))
    print("if or ifでの合計時間は{}[s]".format(t[2]))
    print("if and ifでの合計時間は{}[s]".format(t[3]))
    
    return

if __name__ == "__main__" :
    main()
    
    

#結果
#よくわかんなかったぁ
#理由
#　matplotlibの数値の刻み値が粗い。もっと細かくしてほしい。
#　＝＝だけは少し多そうかなとも思ったけど誤差？
#　100個のデータによる図示は少し多すぎた。

