#1
def num(a):
    if a % 2 == 0:
        print("%d는 짝수입니다" %a)
    else:
        print("%d는 홀수입니다" %a)
        

num(5)


#2
def avr(*arr):
    sum = 0
    for i in arr:
        sum += i
        
    return sum / len(arr)
    
print(avr(1,2,3,4,5,6,7,8))


#3
input1 = input("첫번째 숫자 입력:")
input2 = input("두번째 숫자 입력:")

total = int(input1) + int(input2)
print(total)


#4

