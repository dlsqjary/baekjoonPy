T = int(input())
for i in range(T):
    a,b = map(int, input().split())
    money = 0
    if a == 1:
        money += 5000000
    elif 1<a and a<= 3:
        money += 3000000
    elif 3<a and a<=6:
        money += 2000000
    elif 6<a and a<=10:
        money += 500000
    elif 10<a and a<=15:
        money += 300000
    elif 15<a and a<=21:
        money += 100000
    else:
        money += 0
    if b == 1:
        money += 51200000
    elif 1<b and b<= 3:
        money += 2560000
    elif 3<b and b<=7:
        money += 1280000
    elif 7<b and b<=15:
        money += 640000
    elif 15<b and b<=31:
        money += 320000
    else:
        money += 0
    print(money)

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