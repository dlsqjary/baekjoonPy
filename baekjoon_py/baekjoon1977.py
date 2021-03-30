n = int(input())
k = int(input())
a = 0
li = []
while a*a < k:
    a += 1
    if a*a >= n and a*a <= k:
        li.append(a*a)
if len(li) != 0:
    print(sum(li))
    print(min(li))
else:
    print(-1)