a, b = map(int, input().split())
num_list = []
cnt1 = 0
cnt2 = 1
sum = 0
while len(num_list) < 1000 :
    if cnt1 == cnt2 :
        cnt1 = 0
        cnt2 += 1
    num_list.append(cnt2)
    cnt1 += 1

for i in range(a-1, b):
    sum += num_list[i]

print(sum)