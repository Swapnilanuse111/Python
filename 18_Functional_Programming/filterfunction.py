#filter function it is inbuild function that is used to select only thoes element from a collection that saticefy a given function
l=["python","is","Verry","easy","programming","language"]
var=list(filter(lambda i:len(i)>4 ,l))
print(var)