numRows = 5

# 1 Solution
# res = []
#
# for line in range(1, numRows + 1):
#     c, temp = 1, []
#     for j in range(1, line + 1):
#         temp.append(c)
#         c = int(c * (line - j) / j)
#     res.append(temp)

"""
https://en.wikipedia.org/wiki/Pascal%27s_triangle

c(n, k) = n! / ( k! * (n - k)! )

"""
from math import factorial
res = []
for n in range(numRows):
    c, temp = 1, []
    for k in range(1, n + 1):
        c = int(factorial(n) / (factorial(n - k) * factorial(k)))
        temp.append(c)
    temp.insert(0, 1)
    res.append(temp)
print(res)



