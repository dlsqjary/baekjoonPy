import math
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    ans = math.factorial(M) // (math.factorial(M-N) * math.factorial(N))
    print(ans)

"""
아 처음에 nCa가 n! / a! 인걸로 기억해서 헤맴...
"""