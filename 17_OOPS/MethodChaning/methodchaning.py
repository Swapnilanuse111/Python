#Method Chananing is the process of generating the sequence of execution from child class to parent class
class A:
    def Tata(self):
        print("Call From Tata Company")
class B(A):
    def Infosys(self):
        print("Call From Infosys Comany")
class C(B):
    def Wipro(self):
        print("Call From Wipro Comany")
        super().Infosys
        super().Tata
B.C
print(B.Wipro)
