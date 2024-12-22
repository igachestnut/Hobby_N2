S = input()
cnt = [0] * 26
for c in S:
    cnt[ord(c) - ord("a")] += 1
print(cnt)
cnt2 = [0] * 101
for c in cnt:
    if c > 0:
        cnt2[c] += 1
    print(f"cの値は{c}")
    print(f"cnt2の値は{cnt2}")
print(cnt2)
print("Yes" if all(c in (0, 2) for c in cnt2) else "No")
