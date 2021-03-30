n = input()
arr = [0]* 26
max_num = 0
idx = 0
count = 0
a = n.lower()

for i in a:
    arr[ord(i) - 97] += 1
    if arr[ord(i) - 97] > max_num:
        max_num = arr[ord(i) - 97]


for i in range(len(arr)):
    if arr[i] == max(arr):
        count += 1
        idx = 97 + i

if count >= 2:
    print('?')
else:
    print(chr(idx).upper())







