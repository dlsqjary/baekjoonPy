
T = int(input())
li = [0] * T
for i in range(T):
    a,b = map(int, input().split())
    if a == 1:
        li[i] += 5000000
    elif 1<a and a<= 3:
        li[i] += 3000000
    elif 3<a and a<=6:
        li[i] += 2000000
    elif 6<a and a<=10:
        li[i] += 500000
    elif 10<a and a<=15:
        li[i] += 300000
    elif 15<a and a<=21:
        li[i] += 100000
    else:
        li[i] += 0

    if b == 1:
        li[i] += 51200000
    elif 1<b and b<= 3:
        li[i] += 2560000
    elif 3<b and b<=7:
        li[i] += 1280000
    elif 7<b and b<=15:
        li[i] += 640000
    elif 15<b and b<=31:
        li[i] += 320000
    else:
        li[i] += 0
for i in range(T):
    print(li[i])

"""
1780000
620000
1140000
420000
820000
620000

1780000
620000
1140000
420000
820000
620000
"""