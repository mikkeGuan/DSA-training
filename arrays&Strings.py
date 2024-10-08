A = [1,2,3]
print(A)

#Append O(1)
A.append(12)
print(A)

#Delete from the end O(1)
A.pop()
print(A)

#Insert not in the end O(n)
A.insert(0,0)
print(A)

#Modify an element O(1)
A[0] = 100000
print(A)

#Check length O(1)
print(len(A))
#Check if contains element O(n)
if 0 in A:
    print("True")
else:
    print("False")
    
#Append to end of string O(n)
greeting = "Hello"
newGreeting = greeting + " World"
print(newGreeting)

#Checking if string contains substring O(n)
if "W" in newGreeting:
    print("True")
else:
    print("False")
    
#Accessing characters in string O(1)
print(newGreeting[0:4])

#Len of string O(1)
print(len(newGreeting))