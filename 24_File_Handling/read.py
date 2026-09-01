f=open('data.txt','w+')
data="ABCD"
f.write(data)

data=f.read()
print(data)
f.close()