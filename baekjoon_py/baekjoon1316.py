N = int(input())
#N = 1
cnt = 0
for _ in range(N):
    data = input()
    #data = 'happy'
    temp = 0
    for i in range(len(data)):
        if data.find(data[i], i+1) - i > 1 : #  .find(찾을 문자열, 시작점)
            temp = 0
            break
        else:
            temp = 1

    if temp == 1 :
        cnt += 1

print(cnt)

"""
https://zifmfmphantom.tistory.com/68

find()함수 -> 해당 값이 있으면 그 위치를 반환. 만약 찾는 문자가 없으면 -1을 출력 ( index함수는 ValueError 발생 )
data.find(data[i], i+1) - i > 1  같은 문자의 위치와 현재 문자의 위치를 빼서 그 차이를 확인
a.find('k', 1, 5) -> a변수에서 1~5번째 사이에 'k'가 있는지 확인
"""