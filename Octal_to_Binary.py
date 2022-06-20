def convert(octal):
    i = 0
    decimal = 0
    while octal != 0:
        digit = octal % 10
        decimal += digit * pow(8, i)
        octal //= 10
        i += 1
    binary = 0
    rem = 0
    i = 1

    while decimal != 0:
        rem = decimal % 2
        decimal //= 2
        binary += rem * i
        i *= 10
    print(binary)


n=int(input())
for i in range(n):
    octal=int(input())
    convert(octal)