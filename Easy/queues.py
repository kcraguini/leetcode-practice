import collections
queue = collections.deque()

#Creates the queue
queue = collections.deque([1,2,3])
print(queue)

#Attaches 4 and 5 to the end of the queue
queue.append(4)
queue.append(5)
print(queue)

# Takes out the 1 and 2
queue.popleft()
print(queue)
queue.popleft()
print(queue)


print(queue[0])

print(len(queue))
