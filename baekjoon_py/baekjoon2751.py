import sys  # 시간초과를 방지하기 위해 sys 사용
N = int(input())
li = []
for i in range(N):
    li.append(int(sys.stdin.readline()))

for i in sorted(li):
    sys.stdout.write(str(i) + '\n')


# 기존에 작성한 코드
"""
N = int(input())
li = []
for i in range(N):
    a = int(input())
    li.append(a)

li.sort()
for i in li:
    print(i)
"""