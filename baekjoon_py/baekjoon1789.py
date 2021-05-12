S = int(input())
N = 1
cnt = 0
sum = 0
while True:
    sum += N
    if sum > S:
        print(cnt)
        break
    N += 1
    cnt += 1