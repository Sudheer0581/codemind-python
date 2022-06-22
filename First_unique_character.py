n=input()
s=0
for i in n:
    if n.count(i)==1:
        print(i)
        s=1
        break

    print("-1")
