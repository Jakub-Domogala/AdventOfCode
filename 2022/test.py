from queue import PriorityQueue

q = PriorityQueue()

q.put(1)
q.put(1)
q.put(2)


print(q.get())
print(q.get())
print(q.empty())
print(q.get())
print(q.empty())
