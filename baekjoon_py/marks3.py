marks = [80, 48, 98,74, 35]
for number in range(len(marks)):
    if marks[number] > 60:
        print("%d번 학생은 합격입니다." % (number+1) )

numbers = [1,2,3,4,5]
result = [n*2 for n in numbers if n % 2 == 1]
print(result)
    
