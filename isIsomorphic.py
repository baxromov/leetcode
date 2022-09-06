s = "paper"
t = "title"


def isIsomorphic(s: str, t: str) -> bool:
    if len(t) != len(s):
        return False
    temp = {}
    for i in range(len(s)):
        char1, char2 = s[i], t[i]
        if char1 not in temp:
            if char2 in temp.values():
                return False
            temp[char1] = char2
        elif temp[char1] != char2:
            return False
    return True
a = isIsomorphic(s, t)
print(a)
