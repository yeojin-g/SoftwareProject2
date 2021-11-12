from math import factorial as fact


def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r


def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r


def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r


def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return "Error!"

    if n >= 4000:
        return "Error!"

    romans = {
        1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
        50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
    }

    result = ""
    for value in sorted(romans.keys(),reverse = True):
        while n >= value:
            result += romans[value]
            n -= value
    return result


def romanToDec(romanStr):
    temp = romanStr
    romans = {
        1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
        50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
    }

    result = 0
    for value in sorted(romans.keys(),reverse = True):
        while temp.startswith(romans[value]):
            result += value
            temp = temp[len(romans[value]):]

    if temp != "":
        return "Error!"

    else:
        return result