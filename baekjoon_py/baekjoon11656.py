arr = str(input())
result = []

for i in arr:
    result.append(arr)
    arr = arr[1:]       # 이 부분이 핵심!!  arr = arr[1:]으로 계속 초기화 해주면서 글자를 하나씩 빼줌

result.sort()
for i in result:
    print(i)