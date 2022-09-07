s = "paper"
t = "title"


def isIsomorphic1(s: str, t: str) -> bool:
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


def isIsomorphic2(s: str, t: str) -> bool:
    m1, m2 = {}, {}
    for i in range(len(s)):
        c1, c2 = s[i], t[i]
        if (c1 in m1 and m1[c1] != c2) or (c2 in m2 and m2[c2] != c1):
            return False
        m1[c1] = c2
        m2[c2] = c1
    return True


def isIsomorphic(s: str, t: str) -> bool:
    m1, m2 = {}, {}
    for c1, c2 in zip(s, t):
        if (c1 in m1 and m1[c1] != c2) or (c2 in m2 and m2[c2] != c1):
            return False
        m1[c1] = c2
        m2[c2] = c1
    return True


a = isIsomorphic(s, t)
print(a)
