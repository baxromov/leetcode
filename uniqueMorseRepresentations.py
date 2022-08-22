morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
         ".--.",
         "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
alphabet = (chr(i) for i in range(97, 123))
data = dict(zip(alphabet, morse))
words = ["gin", "zen", "gig", "msg"]
f = ''
for k, v in data.items():
    for i in words:
        for j in i:
            if j == k:
                f += v

print(f)