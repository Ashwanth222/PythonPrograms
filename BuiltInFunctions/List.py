str = "hello"
print(list(str))

languages = ['Python', 'Java', 'JavaScript']
print(len(languages))

testList = []
print(testList, 'length is', len(testList))

testList = [1, 2, 3]
print(testList, 'length is', len(testList))

testTuple = (1, 2, 3)
print(testTuple, 'length is', len(testTuple))

testRange = range(1, 10)
print('Length of', testRange, 'is', len(testRange))

testString = ''
print('Length of', testString, 'is', len(testString))

testString = 'Python'
print('Length of', testString, 'is', len(testString))

# byte object
testByte = b'Python'
print('Length of', testByte, 'is', len(testByte))

testList = [1, 2, 3]

# converting to bytes object
testByte = bytes(testList)
print('Length of', testByte, 'is', len(testByte))

testSet = {1, 2, 3}
print(testSet, 'length is', len(testSet))

# Empty Set
testSet = set()
print(testSet, 'length is', len(testSet))

testDict = {1: 'one', 2: 'two'}
print(testDict, 'length is', len(testDict))

testDict = {}
print(testDict, 'length is', len(testDict))

testSet = {1, 2, 3}
print(testSet, 'length is', len(testSet))

# Empty Set
testSet = set()
print(testSet, 'length is', len(testSet))

testDict = {1: 'one', 2: 'two'}
print(testDict, 'length is', len(testDict))

testDict = {}
print(testDict, 'length is', len(testDict))

testSet = {1, 2}
# frozenSet
frozenTestSet = frozenset(testSet)
print(frozenTestSet, 'length is', len(frozenTestSet))

class Session:
    def __init__(self, number = 0):
        self.number = number

    def __len__(self):
        return self.number


# default length is 0
s1 = Session()
print(len(s1))

# giving custom length
s2 = Session(6)
print(len(s2))

testSet = {1, 2}
# frozenSet
frozenTestSet = frozenset(testSet)
print(frozenTestSet, 'length is', len(frozenTestSet))

# Python List index()
# Python List append()
# Python List extend()
# Python List insert()
# Python List remove()
# Python List count()
# Python List pop()
# Python List reverse()
# Python List sort()
# Python List copy()
# Python List clear()

# merge two lists

list_1 = [1, 'a']
list_2 = [3, 4, 5]

list_joined = list_1 + list_2
print(list_joined)

list_1 = [1, 'a']
list_2 = range(2, 4)

list_joined = [*list_1, *list_2]
print(list_joined)

list_1 = [1, 'a']
list_2 = [1, 2, 3]

list_joined = list(set(list_1 + list_2))
print(list_joined)

list_1 = [1, 'a']
list_2 = [1, 2, 3]

list_2.extend(list_1)
print(list_2)