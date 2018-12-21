# 5 kyu

# The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned. The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.

# Note: Try without using "{:02X}".format(clamp(decimal)).....

# 1. Divide the decimal number by 16. Treat the division as an integer division.
# 2. Write down the remainder (in hexadecimal).
# 3. Divide the result again by 16. Treat the division as an integer division.
# 4. Repeat step 2 and 3 until result is 0.
# 5. The hex value is the digit sequence of the remainders from the last to first.


def rgb(r, g, b):
    r = validateDecimal(r)
    g = validateDecimal(g)
    b = validateDecimal(b)
    print(decimalToHex(r) + decimalToHex(g) + decimalToHex(b))
    return decimalToHex(r) + decimalToHex(g) + decimalToHex(b)


def decimalToHex(decimal):
    hexValue = []
    hexLookUpArray = ["0", "1", "2", "3", "4", "5", "6",
                      "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    while True:
        quotient = decimal / 16
        remainder = decimal % 16
        decimal = quotient
        hexValue.insert(0, hexLookUpArray[remainder])
        if (quotient == 0):
            break
    if len(hexValue) == 1:
        hexValue.insert(0, "0")
    return "".join(hexValue)


def validateDecimal(decimal):
    if decimal < 0:
      decimal = 0
    if decimal > 255:
      decimal = 255
    return decimal


if __name__ == "__main__":
    rgb(0, 0, 0)  # "000000"
    rgb(1, 2, 3)  # "010203"
    rgb(255, 255, 255)  # "FFFFFF"
    rgb(254, 253, 252)  # "FEFDFC"
    rgb(-20, 275, 125)  # "00FF7D"
