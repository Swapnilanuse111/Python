#in general copy if any changes are made to distination 
#varible it will affect source varible becous both sotre same reference address
a=[1,2,3,4,5,6] #sourse varible 
b=a
b[3]=100
print(a)
print(b)