n = int(input())
num_list = list(map(int, input().split()))

max = num_list[0]
min = num_list[0]
num_list.sort()
print(num_list[0] , num_list[n-1])

"""
n = int(input())
num_list = list(map(int, input().split()))

max = num_list[0]
min = num_list[0]

for num in num_list:
    if num > max:
        max = num
    elif num <min:
        min = num
        
print(min, max)

"""
