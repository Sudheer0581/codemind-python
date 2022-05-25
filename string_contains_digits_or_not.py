n=int(input())
for i in range(n):
    m=input()
    for i in m:
        if i in '1234567890':
            print("Yes")
            break
    else:
        print("No")