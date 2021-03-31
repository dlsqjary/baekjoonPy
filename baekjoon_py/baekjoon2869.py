import math
a, b, v = map(int, input().split())
day = (v-b)/(a-b)
print(math.ceil(day) )


""""
시간초과 발생하는 코드

a, b, v = map(int, input().split())
sum = 0
day = 0

while True:
    day += 1
    sum += a
    if sum >= v:
        print(day)
        break
    sum -= b
"""

