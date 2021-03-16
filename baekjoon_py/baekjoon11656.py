arr = str(input())
result = []

for i in arr:
    result.append(arr)
    arr = arr[1:]

result.sort()
for i in result:
    print(i)