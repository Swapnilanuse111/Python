#search()-->it is an inbult function which is avalabe in re module which is used to find the occurece from string in string 
#It Is Find From The Anywhere The Occurence is Present it will give the output if the ocuurece is not presnet in the string it will give none

import re

text="Python Is Very Very Easy Language"
data=re.search(r"abc",text)
print(data)