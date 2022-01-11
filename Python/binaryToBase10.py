def split(word):
    return [char for char in word]


def getbinString():
    binString = str(input("Enter 8-bit binary string: "))
    return binString


binString = getbinString()


binStringSplit = split(binString)


def calcBin():
    binStringArr = list()
    for i in binStringSplit:
        i = int(i)
        binStringArr.append(i)

    for i in binStringArr:
        if (i < 0 or i > 1):
            print("This isn't binary!")
            return

    if (not(binStringArr.__len__() == 8)):
        print("Not enough or too much binary!")
        return
    var1 = binStringArr[7]
    var2 = binStringArr[6]
    var3 = binStringArr[5]
    var4 = binStringArr[4]
    var5 = binStringArr[3]
    var6 = binStringArr[2]
    var7 = binStringArr[1]
    var8 = binStringArr[0]

    base10Result = var1 * 1 + var2 * 2 + var3 * 4 + var4 * \
        8 + var5 * 16 + var6 * 32 + var7 * 64 + var8 * -128

    print(f"{binString} is {base10Result} in base 10.")


calcBin()
