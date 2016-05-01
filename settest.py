import sets

#initializes a set with 5 numbers, an empty set, and one with mixed types
A = sets.Set([1,2,3,4,5])
print(A)

B = sets.Set([])
print(B)

C = sets.Set(["cat", 13])
print(C)

#adds a value not in the set and in the set
A.add(6)
A.add(1)
print(A)

#removes a value not in the set and in the set
A.remove(6)
A.remove(5)
print(A)
A.remove(10)

#prints the size of all the sets
print(A.size(), B.size(), C.size())

#test the union, intersection, and subtract functions
D = sets.Set([2,4,6,8,10])
E = sets.Set([1,2,3,4,5,6,7,8,9,10])
print(D | E)
print(D & E)
print(E - D)

