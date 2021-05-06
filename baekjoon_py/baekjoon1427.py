N = int(input())
A = list(map(int, str(N)))  #입력받은 수를 리스트에 넣어줌 str()을 사용해서 숫자를 문자열로 변환
A.sort(reverse=True) # 내림차순 정렬  .sort(reverse=True)
for i in A:
    print(i, end="")