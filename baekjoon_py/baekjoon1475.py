n = input()
li = [0]*10
six_nine=  0

for i in range(10):
  li[i] = n.count(str(i))
  if i == 6 or i == 9:
    li[i]=  0
    six_nine += n.count(str(i))

max_num = max(li)

if six_nine % 2 == 0:
  six_nine //= 2
else:
  six_nine = six_nine // 2 + 1

answer = max(six_nine, max_num)
print(answer)

#처음 짠 코드
"""
N = list(map(int, input()))
li = [0] * 10
set = 0
max_cnt = 0
six_nine = 0
for i in N:
    if i == 6 or i == 9:
        six_nine += 1
    else:
        li[i] += 1

if six_nine % 2 == 0:
    six_nine //= 2
else:
    six_nine //= 2
    six_nine += 1

if six_nine > max_cnt:
    set = six_nine
else:
    set = max_cnt

print(set)
"""