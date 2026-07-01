#deep copy is type of copy operation which cpoies all element giving them a complitly new address 
# including linnear list as weeel as  nested list aslo
import copy
a=[10,20,30,[12,30],4,44]
b=copy.deepcopy(a)
b[3][0]=100 #is other cases like shallow or genral here the nested values aslo change for the source becous of there
print("Source Output")
print(a)
print("Destination Output")
print(b)