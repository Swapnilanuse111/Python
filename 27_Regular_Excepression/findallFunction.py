#findall()-->Function It Is a type of function which is used in order to find the text or occurence inside the text
#it gives the multiple ocuurec with same name/text 

import re

text="swapnil anuse is verry inteligent boy and aslo he is good english communicator"
data=re.findall(r"is",text)
print(data)