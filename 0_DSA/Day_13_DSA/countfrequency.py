s="hello"
freq={}
for i in s:  #the for loop travers the all string and chaking each and every element
    print(freq)
    if i in freq: #first i=h it is not in freq dictionary
        freq[i]=freq[i]+1 
    else:
        freq[i]=1 #it will add fre[i]=1 means freq={h:1}
print(freq)