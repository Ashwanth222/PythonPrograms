from collections import deque

Deque = deque()

Deque.append('3')
Deque.insert(4, '6')
print(Deque)
print(Deque)
Deque.extend(['4', '5', '6'])
print(Deque)
print(Deque.index('4'))

Deque1 = Deque.copy()
print(Deque1)

Deque1.insert(3,'5')
print(Deque1)

Deque1.reverse()
print(Deque1)

Deque.pop()
print(Deque)
Deque.pop()
print(Deque)
Deque.pop()
print(Deque)