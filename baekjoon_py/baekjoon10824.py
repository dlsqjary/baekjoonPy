A, B, C, D = map(int,input().split())

sum1, sum2 = '', ''
result = 0
sum1 = str(A) + str(B)
sum2 = str(C) + str(D)

result = int(sum1) + int(sum2)
print(result)

"""
map(f, iterable) => map(변환 함수, 순회 가능한 데이터)

함수(f)와 반복 가능한(literable) 자료형을 입력으로 받는다.
map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.

"""