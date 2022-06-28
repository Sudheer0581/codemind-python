s=input()
for i in s:
    if(s.count(i)==1):
        print(s.index(i))
        break
else:
    print("-1")