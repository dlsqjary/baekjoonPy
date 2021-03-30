"""
규칙을 이해하기 어려웠던 문제.
남들이 올려높은 코드를 봐도 잘 모르겠었다.
주말에 다시 풀기
21.03.25
"""
n = int(input())

line = 0
max_num = 0

while n > max_num:
    line += 1
    max_num += line

count = max_num - n

if line % 2 == 0:
    i = line - count
    j = count + 1
else:
    i = count + 1
    j = line - count

print(f'{i}/{j}')

"""
# f-string
형식지정자 %d와 비슷
1)문자열을 지정하는 따오ㅑㅁ표 앞에 f를 접두사로 붙인다.
2)문자열 안에서 중괄호{ }를 이용해서 변수나 계산식을 입력할 수 있다.
print(f'{i}/{j}')
"""