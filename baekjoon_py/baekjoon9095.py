T = int(input())
input_data = []
for i in range(T):
    input_data.append(int(input()))

d = [1,2,4]

for i in range(3, max(input_data)):
    d.append((d[i-1] + d[i-2] + d[i-3]))

for i in input_data:
    print(d[i-1])

"""
정수를 1,2,3의 합으로 나타내는 방법의 수
1: d[n-1] 
2: d[n-2]
3: d[n-3]

max(input_data)로 입력받는 테스트케이스에서 가장 큰 수 만큼 for문이 반복되면서
방법의 수를 저장하는 리스트에 값을 넣음
"""