arr = input()
outputString = []
for i in arr:
    if i >= 'a' and i <= 'm':
        outputString.append(chr(ord(i) + 13))
    elif i >= 'A' and i <= 'M':
        outputString.append(chr(ord(i) + 13))
    elif i >= 'n' and i <= 'z':
        outputString.append(chr(ord(i) - 13))
    elif i >= 'N' and i <= 'Z':
        outputString.append(chr(ord(i) - 13))
    else:
        outputString.append(i)

for i in outputString:
    print(i, end ="")