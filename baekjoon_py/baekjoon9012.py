n = int(input())

for i in range(n):
    stack = []
    st = input()
    cnt = 0
    for j in st:
        if j == '(':
            stack.append(j)
        if j == ')':
            if len(stack) == 0:
                print("NO")
                cnt = 1
                break
            else:
                stack.pop(-1)
    if len(stack) != 0 and cnt == 0:
        print("NO")
    elif len(stack) == 0 and cnt == 0:
        print("YES")
    
