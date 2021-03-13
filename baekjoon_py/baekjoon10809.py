import string

str = input()
result_arr = string.ascii_lowercase
for i in result_arr:
    print(str.find(i), end=' ')  # 문자열.find() 함수는 문자열의 index위치를 반환하고 없는 값이면 -1 리턴

"""
string.ascii_lowercase 소문자 데이터를 상수로 정의해 놓은 것

문자열.find() 함수는 문자열의 index위치를 반환하고 없는 값이면 -1을 반환

## find() 함수만 알고 있었으면 어렵지 않은 문제.
## string 관련 함수를 사용하고 싶으면 string을 import해야함

## string 모듈
import string 

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789
"""