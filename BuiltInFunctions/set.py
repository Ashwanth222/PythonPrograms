list_numbers = [1, 2, 3, 4, 2, 5]

# create set from list
numbers_set = set(list_numbers)
print(numbers_set)

# Output: {1, 2, 3, 4, 5}

# empty set
print(set())

# from string
print(set('Python'))

# from tuple
print(set(('a', 'e', 'i', 'o', 'u')))

# from list
print(set(['a', 'e', 'i', 'o', 'u']))

# from range
print(set(range(5)))

# from set
print(set({'a', 'e', 'i', 'o', 'u'}))

# from dictionary
print(set({'a':1, 'e': 2, 'i':3, 'o':4, 'u':5}))

# from frozen set
frozen_set = frozenset(('a', 'e', 'i', 'o', 'u'))
print(set(frozen_set))

class PrintNumber:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num

# print_num is an iterable
print_num = PrintNumber(5)

# creating a set
print(set(print_num))