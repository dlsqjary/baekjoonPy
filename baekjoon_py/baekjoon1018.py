N, M = map(int, input().split())
# N = 열 갯수  M = 행 갯수
data = list()
for i in range(N):
    data.append(input())
ans = list() # 결과값들을 저장할 리스트

for i in range(N-7):
    for j in range(M-7):
        Black_cnt = 0
        White_cnt = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:   # 첫 번째 색이 'B'인지 'W'인지 2가지로 구분
                    if data[a][b] != 'W':
                        White_cnt += 1
                    if data[a][b] != 'B':
                        Black_cnt += 1
                else:    # 첫 번째 색이 'B'인지 'W'인지 2가지로 구분
                    if data[a][b] != 'W':
                        Black_cnt += 1
                    if data[a][b] != 'B':
                        White_cnt += 1
        ans.append(Black_cnt)
        ans.append(White_cnt)
print(min(ans)) # 각 경우에서 최소값을 찾아서 출력