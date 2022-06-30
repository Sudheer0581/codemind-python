n=input()
s=n.split()
for i in range(len(s)):
    if i%2==0:
        s[i]=str(s[i])
        print(s[i][::-1],end=' ')
    else:
        print(s[i],end=' ')