import math
n , k = map(int, input().split())
answer = math.factorial(n) // (math.factorial(n-k) * math.factorial(k))
print(answer)