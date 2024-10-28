#Fibonacci example
#F(0) = 0
#F(1) = 1
#F(n) = F(n-1) + F(n-2)

#Time: O(2^n), Space complexity: O(n)
def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1) + F(n-2)

print(F(1))


#Linked list example

class SinglyNode:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next    
        def __str__(self):
            return str(self.val)
            
Head = SinglyNode(1)
A = SinglyNode(2)
B = SinglyNode(3)
C = SinglyNode(6)
D = SinglyNode(223)
E = SinglyNode(10000)

Head.next = A
A.next = B
B.next = C
C.next = D
D.next = E 

print(Head)

#Linked list recussion example

#Time: O(n), Space complexity: O(n)
def reverse(node):
    if not node:
        return
    
    reverse(node.next)
    print(node)

reverse(Head)
