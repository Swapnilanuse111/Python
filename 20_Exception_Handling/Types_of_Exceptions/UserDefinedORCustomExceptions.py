'''
    Predifined Excption?
----->This Are The type Of Exception Which are created by the user specicificllly to be used in project
    
      In Order to Crate A userdefined function or custom function a refrrence from Exception Class is used 
'''

class Custom_Error(Exception):
    pass
age=2
if age>18:
    print("The User is Eligible For Voting")
else:
    raise Custom_Error   #Basically it is used in order to raise the user defined excption in any program