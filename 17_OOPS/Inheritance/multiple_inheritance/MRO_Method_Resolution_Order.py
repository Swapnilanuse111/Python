#MRO-Stand For Method Resolution Order Is Way Of Deciding the order of execution In Multiple Inheritance
#MRO Internally Makes Use Of C3 Linnerrization In Order To Create a List of presidence With All the classes Present In a Order
class A:
    pass
class B(A):
    pass
class C(A):
    pass
obj=C()
print(C.mro())