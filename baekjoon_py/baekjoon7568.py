import sys
N = int(sys.stdin.readline())
input_data = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    input_data.append((x, y))

for i in input_data:
    rank = 1
    for j in input_data:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')