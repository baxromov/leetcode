from collections import Counter


def shortestCompletingWord(licensePlate, words) -> str:
    lp = Counter([c for c in licensePlate.lower() if c.isalpha()])
    smallest_word = None

    for word in words:
        if smallest_word is None or len(smallest_word) > len(word):
            wc = Counter(word.lower())
            for c in lp:
                if wc[c] < lp[c]:
                    break
            else:
                smallest_word = word

    return smallest_word