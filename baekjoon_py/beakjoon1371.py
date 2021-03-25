import sys

str = sys.stdin.read()
result_arr = [0]*26  #리스트의 길이를 알파벳 갯수만큼 생성

for i in str:
    if i.islower():
        result_arr[ord(i) - 97] += 1    #문자열 요소를 ord()함수를 사용해 아스키코드값으로 바꾸고 'a'의 아스키코드 값 만큼을 빼줌
                                        #이렇게 하면 해당되는 리스트 인덱스에 값이 카운트됨
for i in range(len(result_arr)):
    if result_arr[i] == max(result_arr):
        print(chr(97+i), end='')

"""
여러줄의 문장을 입력받으려면 
import sys 를 하고
str = sys.stdin.read() 처럼 선언
"""