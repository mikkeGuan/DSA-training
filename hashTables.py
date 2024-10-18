# Hashset

a = set()
print(a)


#Add element to set O(1)
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)
print(a)

#Lookup if exists in set O(1)
if 31 in a:
    print("True")
else:
    print("False")
    

#Remove element from set O(1)
a.remove(3)
print(a)


string ="abcdasdasdasdruichaoguan"
setted = set(string) #Set construction, without duplicates

print(setted)


#Hashmaps - Dictionaries

d = {"a":1, "b":2, "celsius": 3,}
print(d)

#Add key:value to dictionary O(1)
d["apina"] = 6
print(d)

#Lookup if exists in dictionary O(1)
if "apina" in d:
    print("True")
else:
    print("False")

#Check value corresponging to key O(1)
print(d["apina"])

#Loop over the key:val pairs in dictionary O(n)
for key, val in d.items():
    print(f"key {key}: val {val}")
    
#Defaultdict
from collections import defaultdict
default = defaultdict(int)

print(default[2])
print(default)

defaultlist = defaultdict(list)
print(defaultlist)

#Counter
from collections import Counter

counter = Counter(string)
print(counter)
