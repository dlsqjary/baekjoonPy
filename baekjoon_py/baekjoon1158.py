import sys
'''
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
'''
n,k = map(int,input().split())
arr = [i for i]

for i in range(n):
    arr.append(i+1)
    
print('<', end='')
for i in range(n):
    for j in range(k-1):
        arr.append(arr[0])
        arr.pop(0)
    print(', ', end='')
    print(arr.pop(0), end='')
print('>')




n , k = map(int,input().split())
arr = [x for x in range(1,n+1)]
result = []
sibal = k - 1 # 배열 인덱스 0 부터 이므로 -1

for i in range(n):
  if len(arr) > sibal: # 배열이 아직 뽑아야 할 수보다 많다면
    result.append(arr.pop(sibal))
    sibal += k - 1
  
  elif len(arr) <= sibal:
    sibal %= len(arr)
    result.append(arr.pop(sibal))
    sibal += k - 1

print('<',end = '')

for i in result :
  if i == result[-1]:
    print(i,end = '')
  else:
    print("%s, "%(i),end='')
    
print('>')


"""
정답코드
"""
n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]
answer = []
i = 0
for j in range(n):
    i += k-1
    if i >= len(arr):
        i = i%len(arr)
    answer.append(arr.pop(i))
print("<"+str(answer)[1:-1]+">")

"""
시간초과 뜬 코드
"""
n,k = n,k = map(int,input().split())
arr = [i for i in range(1, n+1)]
answer = []
for i in range(n):
    for j in range(k-1):
        arr.append(arr.pop(0))
    answer.append(arr.pop(0))

print("<" + str(answer)[1:-1] + ">")
