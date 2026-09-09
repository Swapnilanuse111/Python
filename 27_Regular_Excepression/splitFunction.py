#split()--->function it is a type of function which to provide the comma whereever you want[in simple word it it used to split the text in diffreent diffrent part with the help of , cooma] 

import re

text="python is verry good and pythoon is easy"
data=re.split(r"and",text)
print(data)