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
        return 'Error!'

    if n >= 4000:
        return 'Error!'

    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value

    return result


def romanToDec(numStr):  # 로마숫자 -> 10진수 변환 알고리즘
    if str(type(numStr)) != "<class 'str'>":  # numStr이 문자열이 아닌 경우 error
        return 'Error!'

    romans = [
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
        ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
        ('X', 10), ('IX', 9), ('V', 5), ('IV', 4),
        ('I', 1)
    ]

    n = 0
    for value, num in romans:
        while numStr.find(value) == 0:
            n += num
            numStr = numStr[len(value):]
    if len(numStr) == 0:
        return n
    else:  # numStr의 길이가 0이 아닌 경우 error
        return 'Error!'


if __name__ == '__main__':
    print(romanToDec("CCXLVIII"))
    print(romanToDec("ABCD"))
    print(romanToDec("123"))
    print(romanToDec(123))
