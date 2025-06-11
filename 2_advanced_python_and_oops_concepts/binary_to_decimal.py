
def binaryToDecimal(binary):
    decimal = 0

    binary  = binary[::-1]

    for i, d in enumerate(binary):
        decimal += int(d)*pow(2, i)
        i += 1
    print (decimal)

if __name__ == "__main__":
    binaryToDecimal("001")
