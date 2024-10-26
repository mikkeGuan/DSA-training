#Stacks (LIFO)

stk = []
print(stk)

#Append to top of stack O(1)
stk.append(1)
stk.append(999)
stk.append(3)
stk.append(-1231123)
stk.append(12)
print(stk)


#Pop from top of stack O(1)
x = stk.pop()

print(x) #Print which element is going to be removed
print(stk)


#Check top of stack O(1)
print(stk[-1])

#Is empty O(1)
if stk:
    print(True)

#Queues (FIFO)

from collections import deque

q = deque()
print(q)

#Add to the right O(1)
q.append(1)
q.append(999)
q.append(3)
print(q)


#Remove from the left O(1)
q.popleft()
print(q)

#Check leftmost element O(1)
print(q[0])

#End of the queue O(1)
print(q[-1])