n = int(input())
a = list(input())
str_len = len(a)
for i in range(n - 1):
    b = list(input())
    for j in range(str_len):
        if a[j] != b[j]:
            a[j] = '?'
print(''.join(a))

"""
아래 코드처럼 하면 답이 ? 로 나오는데 이유를 모르겠음.....
n = int(input())
li = []
for _ in range(n):
    li.append(list(map(str, input().split("\n"))))
a = li[0]
for i in range(1,n):
    b = li[i]
    for j in range(len(a)):
        if a[j] != b[j]:
            a[j] = '?'
print(''.join(a))
"""