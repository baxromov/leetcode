# s = "A man, a plan, a canal: Panamas"
s = "0P"


def isPalindrome(s: str) -> bool:
    s = s.strip().lower()
    tmp = ''
    for i in s:
        if ord(i) in range(97, 123) or ord(i) in range(48, 58):
            tmp += i
    return tmp[::-1] == tmp


a = isPalindrome(s)
print(a)
