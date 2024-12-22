""" #####################################################
発想

- 全体の種類をK以下にしたい。
- 書き換えるボール数を最小にする場合、
    - ある種類において、最も少ないボール数順で書き換える。と答えが出る
##################################################### """
def check() :
    return

from collections import defaultdict
def main() :
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    ball_counts = defaultdict(int)
    for a in A: ball_counts[a] += 1
    counts = [value for value in ball_counts.values()]
    counts.sort()
    while K>0 and counts:
        counts.pop()
        K-=1
    print(sum(counts))
    return


if __name__ == "__main__" :
    main()
    #check()
