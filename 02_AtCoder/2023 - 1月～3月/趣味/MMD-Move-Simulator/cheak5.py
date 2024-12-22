#Newname = input("新しい画像・gif名:{}")
#print(Newname)

a = ["43","34"]
c = "4"
d = "43"
for i in range(len(a)) :
    if c in a[i] :
        print(c)
if c in a :
    print(c)
elif d in a :
    print(d)
else :
    print(a)
#if　見つけたい文字列 in 査定したいリスト:
#これで、for文無しでリストの中に要素が入っているかどうか確認することができる。
