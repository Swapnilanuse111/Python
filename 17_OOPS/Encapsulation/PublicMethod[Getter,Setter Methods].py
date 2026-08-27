
'''Getter Setter Or Public Method Is a Way of assing or Upadting The Private Data Memebers'''
class Bank:
    __a=10
    def getter(self):
        return self.__a

    def setter(self,new):
        self.new=self.__a=new
        return self.new
b=Bank()
print(b.getter())
print(b.setter(30))