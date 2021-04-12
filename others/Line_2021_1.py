table = ["SI JAVA JAVASCRIPT SQL PYTHON C#",
         "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
         "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
         "GAME C++ C# JAVASCRIPT C JAVA"]
language = ['PYTHON','C++', 'SQL']
preference = [7,5, 5]

score = []
arr = []
res = []
ans = [0,0,0,0,0]

for i in range(len(table)):
    arr.append(list(reversed(table[i].split())))

for i in range(len(arr)):
    for j in range(len(arr)):
        for x, y in zip(language,preference):
            if arr[i][j] == x:
                score.append((i,y*(j+1)))
                ans[i] += y*(j+1)

#print(score)
#print(ans)
#print(max(ans))
cnt = 0
idx = 0
n_li = []
temp = []
for i in ans:
    if max(ans) == i:
        cnt += 1
        n_li.append(table[idx].split(' ')[0])
    idx += 1

#print(n_li)

if cnt > 1:
   print(max(n_li))
else:
    print(n_li)


#qweqwwq54169E
#UUUUU
#ZzZz9Z824