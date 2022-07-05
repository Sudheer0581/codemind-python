n=input()
s=n.split()
for i in range(len(s)):
    if i%2!=0:
        continue
    else:
        q=s[i]
        r=q[::-1]
        s[i]=r
print(*s)
        