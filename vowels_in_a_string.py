n=input()
m=input()
for i in range(len(n)):
    if m==n[i]:
        print("True")
        print(i)
        break
else:
    print("False")