#shallow copy dose not affect the linneaar list it crete a diffrent memory addres for linnear list
#however it affect nested list as they share the same reference address
#--for Linnear List
a=[1,2,3,5,6,7]
b=a.copy()
b[4]=100 #in this case the element only change of the destination varible
print(a)
print(b)

#--for Nested List
print("for Nested List")
x=[1,2,3,4,[10,20],7]
y=x.copy()
y[4][0]=2000
print(x)
print(y)