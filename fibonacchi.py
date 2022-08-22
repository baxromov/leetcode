"""
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *
"""
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('*', end=" ")
#     print()
import math
from decimal import Decimal

"""
* * * * * * * * * 
* * * * * * * * 
* * * * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

"""
# for i in range(1, 10):
#     for j in range(1, 10 - i + 1):
#         print('*', end=" ")
#     print()

# n = 8
#
# for i in range(n):
#     for space in range(n-i):
#         print('', end="")
#     for star in range(i+1):
#         print('*', end=" ")
#     print()

# print(sum([i for i in range(int(input()) + 1)]))

# print(Decimal(int(input())*9.8).quantize(Decimal('0.00')))
# s, h = map(int, input().split())
# b = 2 * s / h
# # print(f'{b:.2f}')
#
# from math import sqrt, asin, degrees
# AB = 10
# BC = 10
# AC = sqrt(AB ** 2 + BC ** 2)
# a = round(degrees(asin(AB / AC)))
# b = 180 - 2 * a
# x = 180 - a - b
# print(f'{x}{chr(176)}')
n = 5
print(divmod(177, 10))