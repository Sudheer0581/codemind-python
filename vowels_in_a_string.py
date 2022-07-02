n=input()
a=input()
for i in range(len(n)):
    if(n[i]==a):
        print(True)
        print(i)
        break
else:
    print(False)