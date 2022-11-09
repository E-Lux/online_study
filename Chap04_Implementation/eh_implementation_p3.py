# 통과는 되지만 시간이 오래걸림

from itertools import combinations
from sys import stdin

input = stdin.readline
n, m = map(int, input().split())
one = []
two = []

answer = 1e9

for i in range(n):
    tmp = list(map(int, input().split()))

    for j in range(n):
        if tmp[j] == 1:
            one.append((i,j))
        elif tmp[j] == 2:
            two.append((i,j))


tmp_two = [i for i in range(len(two))]
two_comb = list(combinations(tmp_two,m))

for i in range(len(two_comb)):
    tmp_ans = 0
    for j in range(len(one)):
        tmp = 1e9
        x1, y1 = one[j]
        for l in range(m):
            k = two_comb[i][l]
            x2, y2 = two[k]
            tmp = min(tmp, abs(x1 - x2) + abs(y1 - y2))
        tmp_ans += tmp
    answer = min(answer, tmp_ans)

print(answer)