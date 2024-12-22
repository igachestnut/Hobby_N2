"""
目的
if --- :
  if !!! :
  の処理のスピードと、

if --- and !!! :
の処理スピードの違いを調べたくなった。

条件１
---,!!!の両方の条件が当てはまる時

条件2
---の条件だけ当てはまるとき

"""
#########################################################
import time

def timecheaker(a,b,N) :
    #time1
    start = time.time()
    for _ in range(10^N) :
        if a==b :
            if b :
                pass
    time1 = time.time() - start

    #time2
    for _ in range(10^N) :
        if a or b :
            pass

    time2 = time.time() - start - time1

    #time3
    for _ in range(10^N) :
        if a and b :
            pass

    time3 = time.time() - start - time1 - time2

    #print()
    print(time1)
    print(time2)
    print(time3)
    return

#条件1
a = True
b = True
N = 10000
timecheaker(a,b,N)

##############################################################
#条件2
a = True
b = False

timecheaker(a,b,N)

#予想外の面白い結果が生まれた
#
#ifの査定回数を10**40にしても瞬時に返すということ
#ifの査定回数を10**10000にしてやっと小さな値が生まれた。
#それほどifの処理時間は短いということが分かった。
#
#データにばらつきがあるので、グラフ化しようと思う。
#※次のファイル参照
