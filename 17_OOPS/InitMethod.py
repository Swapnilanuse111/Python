class Demo:
      name="pooja"
      def __init__(self,name,id,sal):
        self.name=name
        self.id=id
        self.sal=sal
s1=Demo("swapnil",101,20000)
s2=Demo("Rahul",102,30000)
print(s1.name)
s1.name="manoj"
print(s1.name)
