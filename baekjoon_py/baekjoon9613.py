n = int(input())
def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

for _ in range(n):
    li = list(map(int, input().split()))
    nn = li.pop(0)
    sum = 0
    for i in range(nn):
        for j in range(nn):
            if i < j:
                sum += gcd(li[i], li[j])
    print(sum)
