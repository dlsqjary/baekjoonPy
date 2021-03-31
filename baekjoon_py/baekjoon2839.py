n = int(input())
box_num = 0

while True:
    if n % 5 == 0:
        box_num = box_num + (n // 5)
        print(box_num)
        break
    n = n-3
    box_num += 1
    if n < 0:
        print(-1)
        break
"""
다시
"""