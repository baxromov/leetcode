import itertools
import operator

data = [3, 4, 1, 5, 6, 7]
string = "Hello World"
dictionary = {"a": 1, "b": 2, "c": 3}
# res = list(itertools.accumulate(string, lambda x, y: x + y))
# res = list(itertools.accumulate(dictionary, lambda x, y: x + y))
# print(res)
# res = itertools.chain(data)
# print(tuple(res))

# a = itertools.cycle(data)
# count = 0
# for i in a:
#     if count > len(data):
#         break
#     print(i)
# #     count += 1
#
# li = [2, 4, 5, 7, 8]
# print(list(itertools.dropwhile(lambda x: x % 2 == 0, li)))








# s = {1, 2}
#
# s.add(3)
# print(s)
# s.update({1,2,3,4,5})
# print(s)
# s.remove(5)
# print(s)
# s.discard(5)
# print(s)
# s.pop()
# print(s)


s1 = {1,2,3}
s2 = {3,4,5}

# union
# res = s1.union(s2)
# res = s1 | s2

# intersection
# res = s1 & s2
# res = s1.intersection(s2)

# difference
# res = s1 - s2
# res = s1.difference(s2)
# res = s1.symmetric_difference(s2)
# res = s1.isdisjoint(s2)
# res = s1.issubset(s2)
# res = s1
#
# print(res)



# print(list(itertools.filterfalse(lambda x: x.startswith('__'), dir(dict))))
#
# my_dict = {1: 'A', 2: 'B', 3: 'C'}
# # my_dict.setdefault(4, 'D')
# t = my_dict.fromkeys({1,2,3,4}, ['salom'])
# print(t)
s = {1,2,3,3, [12334]}
print(s)