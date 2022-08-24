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


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = [[1]]
        l = [1,]
        sum = []
        for i in range(numRows - 1):
            k = n[-1]
            sum = []
            l = []
            for j in range(len(k) - 1):
                sum.append(k[j] + k[j + 1])
                print(sum)
            l.append(1)
            l += sum
            l.append(1)
            n.append(l)
        return n


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        x = [1]
        a = x.copy()
        q = []
        q.append(a)
        for i in range(1, numRows):
            for j in range(1, i):
                if len(x) <= 1:
                    continue
                x[-j] = x[-j] + x[-j-1]
            x += [1]
            a = x.copy()
            q.append(a)
        return q
