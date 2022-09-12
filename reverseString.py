s = ["h","e","l","l","o"]


def reverseString1(s):
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l, r = l + 1, r - 1


def reverseString2(s):
    stack = []
    for c in s:
        stack.append(c)
    i = 0
    while stack:
        s[i] = stack.pop()
        i += 1


def reverseString3(s):
    s[:] = s[::-1]

reverseString3(s)
# reverseString2(s)
print(s)
