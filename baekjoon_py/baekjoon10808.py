str = input()
result_arr = [0]*26  #리스트의 길이를 알파벳 갯수만큼 생성

for i in str:
    result_arr[ord(i) - 97] += 1    #문자열 요소를 ord()함수를 사용해 아스키코드값으로 바꾸고 'a'의 아스키코드 값 만큼을 빼줌
                                    #이렇게 하면 해당되는 리스트 인덱스에 값이 카운트됨
for i in result_arr:
    print(i, end=' ')

"""
파이썬 리스트 개수 만들 때 : arr = [0] * n
for문의 range()함수는 숫자로 범위를 줄 경우에 사용
ord()함수는 문자를 아스키코드 값으로 변환해 주는 함수
"""