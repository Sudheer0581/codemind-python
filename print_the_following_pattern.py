n=int(input())
ascii_value = 65
for i in range(n):
    for j in range(n):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    ascii_value += 1
    print("")