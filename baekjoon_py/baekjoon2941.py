import sys
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
#t = sys.stdin.readline()
#sys.stdin.readline() 하면 갯수가 하나 더 추가되서 나옴. 출바꿈 관련해서 더 카운트 되는듯함.
for i in a:
    s = s.replace(i, "z")
    #t = t.replace(i, "z")
print(len(s))
#(len(t))


"""
lj e s= nj a k

d dz= z=

크로아티아 알파벳	변경
č	                c= 2개
ć	                c- 2개
dž	                dz= 3개
đ	                d- 2개
lj	                lj 2개
nj	                nj 2개
š	                s= 2개
ž	                z= 2개
"""