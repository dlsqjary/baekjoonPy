n = int(input())

for _ in range(n):
    count_arr1 = [0] * 26
    count_arr2 = [0] * 26
    temp = 0
    a, b = map(str, input().split())

    if len(a) == len(b):
        for i in a:
            count_arr1[ord(i) - 97] += 1

        for i in b:
            count_arr2[ord(i) - 97] += 1

        if count_arr1 == count_arr2:
            print("%s & %s are anagrams."%(a,b))
        else:
            print("%s & %s are NOT anagrams."%(a,b))
    else:
        print("%s & %s are NOT anagrams."%(a,b))

"""
아래처럼 하면 안됨!!!
문자열 연결해서 쓸 땐 + 말고 서식지정자 사용할 것
 print(a + " & " + b + " are Not anagrams.")
"""