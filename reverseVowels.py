s = "leetcode"


def reverseVowels(s):
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


w = reverseVowels(s)
print(w)