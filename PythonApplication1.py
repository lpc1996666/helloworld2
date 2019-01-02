i=-1
s='mis*is*p*.'
pos_str=[-1]
for a in s:
    i+=1
    if a=='*':
        pos_str.append(i)
print(pos_str)
str=[]
for k in range(len(pos_str))[:-1]:
    str.append(s[pos_str[k]+1:pos_str[k+1]])
if s[-1]!='*':
    str.append(s[pos_str[-1]+1:])
print(str)
c=0
while 1:
    c+=1
    if c==5:
        break
print(c)
