import sys
N = int(sys.stdin.readline())
li = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    li.append([y, x])

sort_li = sorted(li)

for y, x in sort_li:
    print(x, y)


#https://www.acmicpc.net/problem/11651