s = list("the sring")
h = []
f = 0
for i in range(0,26):
    h.append(0)
for i in range(0,len(s)):
    k = ord(s[i]) - ord('a')
    if k >= 0 and k < 26:
        if h[k] == 0:
            h[k] = 1
        else:
            print("not unique")
            f = 1
            break

if f == 0:
    print("unique")
