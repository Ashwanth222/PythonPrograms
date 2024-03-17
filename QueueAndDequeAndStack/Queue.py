from queue import Queue

Queue = []

Queue.append(1)
print(Queue)
Queue.append(2)
print(Queue)
Queue.append(3)
print(Queue)
Queue.sort(reverse = True)
print(Queue)
Queue.extend([4, 5, 6])
print(Queue)
print(Queue.index(4))

Queue1 = Queue.copy()
print(Queue1)

Queue1.insert(4,5)
print(Queue1)

Queue1.reverse()
print(Queue1)

Queue.pop()
print(Queue)
Queue.pop()
print(Queue)
Queue.pop()
print(Queue)