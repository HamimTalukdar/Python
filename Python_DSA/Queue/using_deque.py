from collections import deque

# Creating an empty queue using deque
queue = deque()

# Enqueueing (adding) elements
queue.append(1)
queue.append(2)
queue.append(3)

# Displaying the queue
print("Queue:", queue)

# Dequeueing (removing) elements
dequeued_element = queue.popleft()
print("Dequeued Element:", dequeued_element)

# Displaying the updated queue
print("Updated Queue:", queue)


if not queue:
    print("Empty")