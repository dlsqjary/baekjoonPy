a= int(input())
arr = [0 for i in range(a+1)]
arr[1] = 0
for i in range(2, a+1):
    arr[i] = arr[i-1] +1
    if i%2 == 0 and arr[i]>arr[int(i/2)]+1:
        arr[i] = arr[int(i/2)]+1
    if i%3 == 0 and arr[i]>arr[int(i/3)]+1:
        arr[i] = arr[int(i/3)]+1
print(arr[a])

"""
다이나믹 프로그래밍 bottom-up방식

arr = [0 for i in range(a+1)]
리스트 arr의 길이를 입력받은 값 +1을 해준다.

arr[i-1] +1
arr[int(i/2)]+1
arr[int(i/3)]+1
위 3가지 식 중에서 최소인 값을 저장 
"""