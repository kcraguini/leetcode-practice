import collections
queue = collections.deque()

# If you want to initialize with numbers
queue = collections.deque([1,2,3,4,5])

# Appending
queue.append(6)
queue.append(7)
print(queue)

# dequeuing
queue.popleft() # 1
queue.popleft() # 2
print(queue)

# checks the front of the queue
queue[0] # 3
print(queue[0])

# checks length
len(queue) # 5
print(len(queue))