# def findWords(words):
#     row_1 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
#     row_2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
#     row_3 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
#     res = []
#     for Word in words:
#         count_1 = 0
#         count_2 = 0
#         count_3 = 0
#         word = Word.lower()
#         for dic in row_1:
#             count_1 = count_1 + word.count(dic)
#         for dic in row_2:
#             count_2 = count_2 + word.count(dic)
#         for dic in row_3:
#             count_3 = count_3 + word.count(dic)
#         if count_1 == len(word) or count_2 == len(word) or count_3 == len(word):
#             res.append(Word)
#     return res




# Solution

# row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
# row2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
# row3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
#
# index_list = []
# new_list = []
#
# for i in words:
#     for j in i:
#         if j.lower() in row1:
#             index_list.append(1)
#         elif j.lower() in row2:
#             index_list.append(2)
#         elif j.lower() in row3:
#             index_list.append(3)
#     result = all(element == index_list[0] for element in index_list)
#
#     if result:
#         index_list.clear()
#         new_list.append(i)
#     else:
#         index_list.clear()
#
# print(new_list)


# Solution 2
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')

        result = []

        for i in words:
            word = set(i.lower())

            if word.intersection(row1) == word:
                result.append(i)
            elif word.intersection(row2) == word:
                result.append(i)
            elif word.intersection(row3) == word:
                result.append(i)

        return result



















