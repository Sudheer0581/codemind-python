for i in range(int(input())):
    hexdecnum = input()
    binnum = ""
    hexlen = len(hexdecnum)
    i = 0
    while i<hexlen:
        if hexdecnum[i] == '0':
            binnum = binnum + "0000"
        elif hexdecnum[i] == '1':
            binnum = binnum + "0001"
        elif hexdecnum[i] == '2':
            binnum = binnum + "0010"
        elif hexdecnum[i] == '3':
            binnum = binnum + "0011"
        elif hexdecnum[i] == '4':
            binnum = binnum + "0100"
        elif hexdecnum[i] == '5':
            binnum = binnum + "0101"
        elif hexdecnum[i] == '6':
            binnum = binnum + "0110"
        elif hexdecnum[i] == '7':
            binnum = binnum + "0111"
        elif hexdecnum[i] == '8':
            binnum = binnum + "1000"
        elif hexdecnum[i] == '9':
            binnum = binnum + "1001"
        elif hexdecnum[i] == 'a' or hexdecnum[i] == 'A':
            binnum = binnum + "1010"
        elif hexdecnum[i] == 'b' or hexdecnum[i] == 'B':
            binnum = binnum + "1011"
        elif hexdecnum[i] == 'c' or hexdecnum[i] == 'C':
            binnum = binnum + "1100"
        elif hexdecnum[i] == 'd' or hexdecnum[i] == 'D':
            binnum = binnum + "1101"
        elif hexdecnum[i] == 'e' or hexdecnum[i] == 'E':
            binnum = binnum + "1110"
        elif hexdecnum[i] == 'f' or hexdecnum[i] == 'F':
            binnum = binnum + "1111"
        i = i+1
    print(binnum)