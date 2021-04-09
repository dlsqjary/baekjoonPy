a = int(input())

arr = [0] * (a + 1)
arr[1] = 1

for i in range(2, a+1):
    arr[i] = arr[i-1] + arr[i-2]
print(arr[a])

"""
이 방법처럼 하게 되면 시간초과가 발생함.
재귀식으로 풀면 중복연산이 많이 발생하기 때문.
배열에 값을 넣으면서 계산하면 중복 연산이 발생하지 않아 문제해결 시간이 더 빠름

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
"""