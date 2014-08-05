s1 = list("This is the string")
while ' ' in s1:
    i = s1.index(' ')
    s1.remove(' ')
    s1.insert(i,"%20")
print(''.join(s1))
