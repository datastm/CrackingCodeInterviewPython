s1 = list("aabcccaaa")
count = 0
tmp = s1[0]
s2 = []
for i in range(0,len(s1)):
    if s1[i] == tmp:
        count += 1
    else:
        s2.append(tmp)
        s2.append(str(count))
        tmp = s1[i]
        count = 1

s2.append(tmp)
s2.append(str(count))        
if len(s1) > len(s2):
    print(''.join(s2))
else:
    print(''.join(s1))
