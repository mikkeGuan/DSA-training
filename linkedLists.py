#Singly linked list

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
D = SinglyNode(555)
E = SinglyNode(10000)

Head.next = A
A.next = B
B.next = C
C.next = D

# print(Head)
 
#Travese list - O(n)
curr = Head

while curr:
    print(curr)
    curr = curr.next
    
#Display linked list -O(n)
def display(head):
    elements = []
    current = head
    while current:
        elements.append(str(current.val))
        current = current.next
   # print("  -> next in the list is:  ".join(elements))

display(Head)

#Search for node - O(n)
def search(head, val):
    current = head
    while current:
        if  val == current.val:
            return True
        current = current.next
        
    return False

result = search(Head, 555)
print(result)


#Doubly linked list

class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
    def __str__(self):
        return str(self.val)
    
head = tail = DoublyNode(1)
print(tail)


#Insert in beginning - O(1)

def insert(head, tail, val):
    new_node = DoublyNode(val, next=head)
    head.prev = new_node
    return new_node, tail

head, tail = insert(head, tail, 0)
display(head)

#Display doubly linked list - O(n)
def displayDoubly(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print("  <--> elements beside each other:  ".join(elements))
    
displayDoubly(head)
    

#Insert at the end - O(1)

def insertEnd(head, tail, val):
    new_node = DoublyNode(val, prev=tail,)
    tail.next = new_node
    return head, new_node

head, tail = insert(head, tail, 111)
display(head)

displayDoubly(head)