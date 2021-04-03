N = int(input())
for _ in range(N):
    li = list(map(int, input().split()))
    a = li.pop(0)
    sum = 0
    for i  in range(a):
        sum += li[i]
    avg = sum / len(li)
    cnt = 0
    for i in range(a):
        if li[i] > avg:
            cnt += 1
    print(str("%.3f" % round((cnt / a) * 100, 3)) + "%")
"""    
아래처럼 하면 백준에서 틀렸다고 뜸
아마 출력하는 부분에서 문제가 있는듯....? 아니면 답 구하는 부분에서 a * 100 이렇게 하면 안된다던가...
    answer = format((cnt  / a *100 ) , ".3f")
    print(answer  , end="%")
"""