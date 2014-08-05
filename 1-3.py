s1 = list("string")
s2 = list("tsrgia")
flag = "is"
if len(s1) == len(s2):
    while len(s2) > 0:
        tmp = s2[0]
        if tmp in s1:
            s2.remove(tmp)
            s1.remove(tmp)
        else:
            flag = "is not"
            break
else:
    flag = "is not"
print(flag)
