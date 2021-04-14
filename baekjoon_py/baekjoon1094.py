x = int(input())
num_list = []
default_num = 64
num_list.append(default_num)

while sum(num_list) > x :
    temp = num_list.pop() // 2
    num_list.append(temp)
    num_list.append(temp)
    if sum(num_list[:-1]) >= x:
        num_list.pop()

print(len(num_list))



"""
처음 짠 코드

X = int(input())
A = 64
cnt = 0
sum_list = []
ans = 0
sum_list.append(A)

while sum(sum_list) > :
    temp = min(sum_list) // 2
    sum_list.append(temp)
    if sum(sum_list) > X :   #  이 부분이 문제였음. if문 조건이 잘못됨
        sum_list.pop(0)
        sum_list.append(temp)
        if sum(sum_list) // 2 >= X :
            ans = sum(sum_list)
        else :
            sum_list.append(temp)

    print(sum_list)

#print(len(sum_list))
"""