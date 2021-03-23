a, b = map(int, input().split())
c,d,e,f,g = map(int, input().split())
sum = a*b
print("%d %d %d %d %d" %(c-sum, d-sum, e-sum, f-sum, g-sum))

"""
%d처럼 서식문자 사용할땐 뒤에 변수들 앞에 % 써야함!
"""