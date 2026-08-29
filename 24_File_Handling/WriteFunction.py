'''write()Function
-------->write Function It is a type of function Which  is Used In order to write the text content inside the file by using python program
--->If Soppos The File Is Not Presnt In the system or floder In The Time Or File Haandling By using the write function it automaticlly creat the new file which is in the give program
---->Whenever I Excecut the perticular program agin and agin The Previous Data or text content Replce or overide by the new data
'''

f=open('abc.txt','w')
data="Swapnil"
f.write(data)
f.close()