N = int(input())
d = [0, 1, 1]       # 리스트 d는 N자리 이친수의 갯수를 저장. 0,1,1은 N의 자릿수를 의미
for i in range(3, N+1):
    d.append(d[i-1] + d[i-2])

print(d[N])