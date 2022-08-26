def findWords(words):
    row_1 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
    row_2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
    row_3 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
    res = []
    for Word in words:
        count_1 = 0
        count_2 = 0
        count_3 = 0
        word = Word.lower()
        for dic in row_1:
            count_1 = count_1 + word.count(dic)
        for dic in row_2:
            count_2 = count_2 + word.count(dic)
        for dic in row_3:
            count_3 = count_3 + word.count(dic)
        if count_1 == len(word) or count_2 == len(word) or count_3 == len(word):
            res.append(Word)
    return res
