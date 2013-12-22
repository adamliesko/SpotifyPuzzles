# takes decimal number as an input and returns its reversed binary representation as a decimal number
def revBinNums(number):
    print(int(bin(int(bin(number)[2:][::-1],2))[2:],2))

revBinNums(int(input()))
