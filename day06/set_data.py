#dict
x = {
    'a':[1,2,3],
    'b':[4,5,6]

}
print(list(x.keys()))  # ['a', 'b']
print(list(x.values()))  # [[1, 2, 3], [4, 5, 6]]
print(list(x.items()))  # [('a', [1, 2, 3]), ('b', [4, 5, 6])]

#set(집합) (중복된 것 출력 x)
a = {1,2,3,1,2,3,1,2,3}
print(a)  # {1, 2, 3}
b = set([1,2,3,5,4,3,2])
b.add(6)
print(b)
b.discard(3)
print(b)
b.clear()
print(b)







