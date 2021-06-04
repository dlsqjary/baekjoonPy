import sys
do_n, do_l = map(int, sys.stdin.readline().split())
do_n_li = []
do_l_li = []

for _ in range(do_n):
    do_n_li.append(str(input()))

for _ in range(do_l):
    do_l_li.append(str(input()))

# 입력받은 리스트를 set()에 넣고 '&'연산자를 통해 공통인 부분을 저장
same = set(do_n_li) & set(do_l_li)

print(len(same))
same = sorted(same)
for i in same:
    print(i)
