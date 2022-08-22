
s = "LIX"

roman_s = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
num = 0

for i in range(len(s)):
    if i > 0 and roman_s[s[i]] > roman_s[s[i - 1]]:
        num += roman_s[s[i]] - 2 * roman_s[s[i - 1]]
    else:
        num += roman_s[s[i]]

print(num)
