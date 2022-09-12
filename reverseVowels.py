s = "leetcode"


def reverseVowels1(s):
    vowels = "aeiouAEIOU"

    slist = list(s)

    l, r = 0, len(slist) - 1

    while l < r:
        if slist[l] not in vowels:
            l += 1
            continue
        if slist[r] not in vowels:
            r -= 1
            continue
        slist[l], slist[r] = slist[r], slist[l]
        l, r = l + 1, r - 1
    return "".join(slist)


def reverseVowels2(s):
    s = list(s)
    s1 = ""
    a = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    aa = []
    for i in range(len(s)):
        for j in range(len(a)):
            if s[i].find(a[j]) >= 0:
                aa.append(i)
    while len(aa) > 0:
        x, y = s[aa[-1]], s[aa[0]]
        s[aa[-1]], s[aa[0]] = y, x
        if len(aa) > 1: aa.pop(-1)
        aa.pop(0)
    for i in range(len(s)):
        s1 += s[i]
    return s1

w = reverseVowels1(s)
print(w)