#Union 
a={10,20,30}
b={50,60,70}
print(a | b)

#Diffrence Opration
a={10,20,700,30}
b={50,60,70}
print(a - b)


#Symmetric-->Returns elements that are in either set but not in both.

A = {1, 2, 3}
B = {2, 3, 4}

print(A ^ B)
print(A.symmetric_difference(B))

#adding the element on set
fruit={"mango","orange"}
fruit.add("banana")
print(fruit)


#Add Multiple Elements (update())

fruit={"mango","orange"}
fruit.update(["saa","pink"])
print(fruit)

#remove an element from the set

fruit={"manago","banana"}
fruit.remove("manago")
print(fruit)


#remove the element form the set using discard

fruit={"fedth","aaa","sasa"}
fruit.discard("aaa")
print(fruit)



