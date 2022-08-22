digits =[9]


def plusOne(digits: list):
    n = len(digits)
    sum = 0
    for i in range(n):
        k = 10 ** (n - i - 1)
        sum += digits[i] * k
    k = 0
    sum += 1
    digits.clear()
    while sum > 0:
        k = sum % 10
        sum //= 10
        digits.append(k)
    digits.reverse()
    return digits


print(plusOne(digits))