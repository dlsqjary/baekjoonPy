x, y = map(int, input().split())
 
a = [1, 3, 5, 7, 8, 10 ,12]
b = [4, 6, 9, 11]
c = 2
 
temp = 0
def result_fuc(a):
    if temp % 7 == 0:
        print('SUN')
    elif temp % 7 == 1:
        print('MON')
    elif temp % 7 == 2:
        print('TUE')
    elif temp % 7 == 3:
        print('WED')
    elif temp % 7 == 4:
        print('THU')
    elif temp % 7 == 5:
        print('FRI')
    elif temp % 7 == 6:
        print('SAT')
        
for i in range(x):
    if i in a:
        temp += 31
    elif i in b:
        temp += 30
    elif i == c:
        temp += 28
 
temp += y
result_fuc(temp)

   
